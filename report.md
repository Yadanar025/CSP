# Project 2 Report: University Class Scheduling & Timetable Optimization

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Total Courses Configured:**`, `**Video Presentation Link:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information 
- **Name:** Khin Yadanar Aung
- **MMDT ID:** MMDT002

---

## Section 1: Dataset & University Configuration
- **Total Courses Configured:** 65
- **Total Rooms Configured:** 20
- **Total Time Slots Configured:** 50

---

## Section 2: Local Verification & Implemented Solvers
*Check the algorithms and features you successfully ran and verified by placing an `x` in the brackets (e.g., `[x]`):*
- [x] DataLoader & CSV Parsing
- [x] Hard Constraint Validation Engine
- [x] Soft Penalty & Quality Evaluation Engine
- [x] CSP Backtracking with MRV + LCV + Forward Checking
- [x] Min-Conflicts CSP Local Search
- [x] Simulated Annealing / Genetic Algorithm Optimizer
- [x] Timetable CSV Export (<studentid>_timetable.csv)

---

## Section 3: Video Presentation & Project Structure
- **Video Presentation Link:** https://drive.google.com/file/d/1SkgzHpn3uh6MikSojEQ-BClOaaagz06Y/view?usp=drive_link
- **Project Directory Structure:** app.py: Main entry point that runs the scheduling process that call scheduler_core, scheduler_solver and scheduler_penalty file. scheduler_core.py: Loads CSV data and builds CSP domains for 20 courses. scheduler_solver.py: Finds a schedule using CSP search and heuristics. scheduler_penalty.py: Evaluates and improves the schedule using soft constraints and simulated annealing. data/: Contains input datasets and the final timetable CSV.

---

## Section 4: Discussion & Problem Formulation
*Provide your written analysis for each point by replacing the bracket placeholders below:*
- **How did you formulate the variables, domains, and constraints for this scheduling problem?**
The variables are the 20 mandatory courses from five student cohorts where Each course has a domain containing possible rooms, instructors, and time slots. The system checks hard   constraints to prevent room clashes, instructor clashes, and overlapping classes for the same cohort. Room capacity is handled as a penalty because some courses have more students than the available rooms can hold. Finally, soft constraints help improve the timetable by reducing overcrowding, building changes, schedule gaps, and consecutive classes.

- **Compare CSP Backtracking (with heuristics) vs Local Search (Min-Conflicts / Simulated Annealing) in terms of scalability and solution quality.**
The variables are the 20 mandatory courses from five student cohorts where Each course has a domain containing possible rooms, instructors, and time slots. The system checks hard   constraints to prevent room clashes, instructor clashes, and overlapping classes for the same cohort. Room capacity is handled as a penalty because some courses have more students than the available rooms can hold. Finally, soft constraints help improve the timetable by reducing overcrowding, building changes, schedule gaps, and consecutive classes.
For Local search methods, Min-Conflicts and Simulated Annealing, improve the schedule through small changes. Simulated annealing checks hard constraints after every change, so it maintains a valid schedule while reducing penalties. In the project, it reduced the penalty from 5168 to approximately 2000 without creating new conflicts.

- **How can modern AI / LLM techniques be combined with CSP solvers for real-world automated university scheduling?**
As LLMs can be advantaged for unstructured information, while CSP can find the solutions that stisfy specific constraints. The combination of LLM and CSP can be applied in using information such as instructors notes, instructors schedule from google, room requirements, and scheduling preferences, may be stored in documents rather than structured databases. 
An LLM can retrieve relevant information and convert it into structured inputs for a CSP solver. The solver can then assign courses to rooms and time slots while considering constraints such as instructor availability, room capacity, and scheduling conflicts. 


