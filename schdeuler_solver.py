
def scheduling_constraint(course_id, candidate, assignment, course_cohort): 
    #check if there is any clash in the room 
    #variable = course id, domain = candidate, constrain = room, instructor, cohort, assignmnet = scheduled course
    room, instr, slot = candidate
    this_cohort = course_cohort.get(course_id)
    for other_id, other_val in assignment.items():
        other_room, other_instr, other_slot = other_val
        if slot != other_slot:
            continue
        if room == other_room:
            return False          # room clash
        if instr == other_instr:
            return False          # instructor clash
        if this_cohort == course_cohort.get(other_id):
            return False          # cohort clash
    return True # retur if no clash

def heuristic_variable_selection(domains, assignment, course_cohort):
    unassigned = [cid for cid in domains if cid not in assignment]  #for checking if the course is assigned or not

    def degree(cid): #Degree of Heristic
        this_cohort = course_cohort.get(cid) 
        return sum(1 for other in unassigned
                   if other != cid and course_cohort.get(other) == this_cohort)
        #Go through all unassigned courses and count every course that is not in same year (CSE 342 that belongs to CSE_Y3.)

    # MRV first (smallest domain), degree heuristic as tie-break (most constrained cohort-mates)
    unassigned.sort(key=lambda cid: (len(domains[cid]), -degree(cid)))  #CSE 588 (5,4), CSE 277 (2,2) 
    return unassigned[0]

def LCV(course_id, domain, assignment, domains, course_cohort): 
    #Choose the candidate that restricts the fewest options for other unassigned courses.
    this_cohort = course_cohort.get(course_id) #to check cohort clash

    # to calculates how many conflicts a particular candidate could cause for other unassigned courses.
    def conflicts_caused(value):
        room, instr, slot = value #separate candidate value
        count = 0
        for other_id, other_domain in domains.items(): #checking if any other course is 
            if other_id == course_id or other_id in assignment: #skip the assigned course
                continue
            for other_room, other_instr, other_slot in other_domain: #check candidate of another course
                if slot != other_slot: #skip different time slot
                    continue
                if room == other_room or instr == other_instr or this_cohort == course_cohort.get(other_id): 
                    #if there is any conflit of above conditions meet count as conflit
                    count += 1
            return count
        return sorted(domain, key=conflicts_caused)  #return least constraint candidate

def forward_check(course_id, value, domains, assignment, course_cohort):
    #remove candidate values that conflict with the newly assigned course.
    room, instr, slot = value #separate candidate value
    this_cohort = course_cohort.get(course_id) #current assigned course 
    removed = {}
    for other_id, other_domain in domains.items():
        if other_id == course_id or other_id in assignment: #remove the current candidate
            continue
        new_domain = [
            v for v in other_domain #v = (room, instructor, slot)
            if not (v[2] == slot and (v[0] == room or v[1] == instr or course_cohort.get(other_id) == this_cohort))
        ]
        if not new_domain:
            return None            # a domain went empty — this branch is dead
        removed[other_id] = new_domain
    return removed #return remaing possible candidate


def backtrack(assignment, domains, course_cohort):
    #schedule courses one by one and choice causes a problem, go back and try another choice
    if len(assignment) == len(domains): #check if all cause are assigned
        return dict(assignment)

    course_id = heuristic_variable_selection(domains, assignment, course_cohort)
    for value in LCV(course_id, domains[course_id], assignment, domains, course_cohort):
        if scheduling_constraint(course_id, value, assignment, course_cohort):
            assignment[course_id] = value
            pruned = forward_check(course_id, value, domains, assignment, course_cohort)
            if pruned is not None:
                new_domains = dict(domains)
                new_domains.update(pruned)
                result = backtrack(assignment, new_domains, course_cohort)
                if result is not None:
                    return result
            del assignment[course_id]
    return None


def backtracking_search(domains, course_cohort):
    return backtrack({}, dict(domains), course_cohort)
