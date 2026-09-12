import os
import re
import pytest

# Resolve the report path.
REPORT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'report.md'))

def get_report_content():
    if not os.path.exists(REPORT_PATH):
        raise AssertionError(f"report.md was not found at {REPORT_PATH}")
    with open(REPORT_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def get_section_discussion_answer(question_keyword, content):
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if question_keyword in line and '**' in line:
            answer_lines = []
            for j in range(i + 1, len(lines)):
                next_line = lines[j].strip()
                # Stop if we hit a new list item, header, or divider
                if next_line.startswith('-') or next_line.startswith('##') or next_line.startswith('---'):
                    break
                if next_line:
                    answer_lines.append(next_line)
            return '\n'.join(answer_lines)
    return None

@pytest.mark.weight(5)
@pytest.mark.number("2.1")
def test_student_information():
    """report.md: Student Information check"""
    content = get_report_content()
    name_match = re.search(r'-\s*\*\*Name:\*\*\s*(.*)', content)
    mmdt_id_match = re.search(r'-\s*\*\*MMDT ID:\*\*\s*(.*)', content)
    
    assert name_match is not None, "Name field not found under Student Information"
    assert mmdt_id_match is not None, "MMDT ID field not found under Student Information"
    
    name = name_match.group(1).strip()
    mmdt_id = mmdt_id_match.group(1).strip()
    
    assert name and name != "[Write your Name here]", "Student Name must be filled out"
    assert not (name.startswith("[") and name.endswith("]")), "Student Name cannot contain placeholder text"
    
    assert mmdt_id and mmdt_id != "[Write your MMDT ID here]", "MMDT ID must be filled out"
    assert not (mmdt_id.startswith("[") and mmdt_id.endswith("]")), "MMDT ID cannot contain placeholder text"

@pytest.mark.weight(5)
@pytest.mark.number("2.2")
def test_dataset_configuration():
    """report.md: Dataset Configuration check"""
    content = get_report_content()
    courses_match = re.search(r'-\s*\*\*Total Courses Configured:\*\*\s*(.*)', content)
    rooms_match = re.search(r'-\s*\*\*Total Rooms Configured:\*\*\s*(.*)', content)
    slots_match = re.search(r'-\s*\*\*Total Time Slots Configured:\*\*\s*(.*)', content)
    
    assert courses_match is not None, "Total Courses Configured field not found"
    assert rooms_match is not None, "Total Rooms Configured field not found"
    assert slots_match is not None, "Total Time Slots Configured field not found"
    
    c_str = courses_match.group(1).strip()
    r_str = rooms_match.group(1).strip()
    s_str = slots_match.group(1).strip()
    
    assert not (c_str.startswith("[") and c_str.endswith("]")), "Total Courses Configured cannot contain placeholder text"
    assert not (r_str.startswith("[") and r_str.endswith("]")), "Total Rooms Configured cannot contain placeholder text"
    assert not (s_str.startswith("[") and s_str.endswith("]")), "Total Time Slots Configured cannot contain placeholder text"
    
    c_match = re.search(r'\d+', c_str)
    r_match = re.search(r'\d+', r_str)
    s_match = re.search(r'\d+', s_str)
    
    assert c_match is not None, "Total Courses Configured must contain a numeric value"
    assert r_match is not None, "Total Rooms Configured must contain a numeric value"
    assert s_match is not None, "Total Time Slots Configured must contain a numeric value"
    
    c_val = int(c_match.group(0))
    r_val = int(r_match.group(0))
    s_val = int(s_match.group(0))
    
    assert c_val >= 15, f"You must configure at least 15 courses (currently: {c_val})"
    assert r_val >= 6, f"You must configure at least 6 rooms (currently: {r_val})"
    assert s_val >= 15, f"You must configure at least 15 time slots (currently: {s_val})"

@pytest.mark.weight(5)
@pytest.mark.number("2.3")
def test_local_verification_checked():
    """report.md: Verification checklist"""
    content = get_report_content()
    checked_algs = re.findall(r'-\s*\[[xX]\]\s*(.*)', content)
    assert len(checked_algs) > 0, "No algorithms or features were checked off as verified (marked with [x])"

@pytest.mark.weight(5)
@pytest.mark.number("2.4")
def test_presentation_information():
    """report.md: Presentation & Project Structure check"""
    content = get_report_content()
    video_match = re.search(r'-\s*\*\*Video Presentation Link:\*\*\s*(.*)', content)
    struct_match = re.search(r'-\s*\*\*Project Directory Structure:\*\*\s*(.*)', content)
    
    assert video_match is not None, "Video Presentation Link field not found"
    assert struct_match is not None, "Project Directory Structure field not found"
    
    video_link = video_match.group(1).strip()
    struct_desc = struct_match.group(1).strip()
    
    assert video_link and not video_link.startswith("["), "Video Presentation Link must be completed and cannot be placeholder"
    assert video_link.startswith("http://") or video_link.startswith("https://"), "Video Presentation Link must be a valid absolute HTTP/HTTPS URL"
    assert struct_desc and not struct_desc.startswith("["), "Project Directory Structure must be completed and cannot be placeholder"

@pytest.mark.weight(10)
@pytest.mark.number("2.5")
def test_formulation_discussion():
    """report.md: CSP Formulation and Discussion check"""
    content = get_report_content()
    discussion_points = [
        "How did you formulate the variables, domains, and constraints for this scheduling problem?",
        "Compare CSP Backtracking (with heuristics) vs Local Search (Min-Conflicts / Simulated Annealing) in terms of scalability and solution quality.",
        "How can modern AI / LLM techniques be combined with CSP solvers for real-world automated university scheduling?"
    ]
    
    for idx, question in enumerate(discussion_points, 1):
        text = get_section_discussion_answer(question, content)
        assert text is not None, f"Discussion question {idx} ('{question}') is missing from report.md"
        text = text.strip()
        assert text != "", f"Discussion question {idx} ('{question}') has not been filled out (it is empty)"
        assert not (text.startswith("[") and text.endswith("]")), f"Discussion question {idx} ('{question}') cannot contain placeholder text"
