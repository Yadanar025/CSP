import os
import sys
import glob
import pytest

@pytest.mark.weight(10)
@pytest.mark.number("1.1")
def test_submitted_files(request):
    """Check that required files and datasets under project directory exist"""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    expected_files = [
        'app.py',
        'report.md',
        'AI_declaration.png',
        'data/courses.csv',
        'data/instructors.csv',
        'data/rooms.csv',
        'data/time_slots.csv',
        'data/student_cohorts.csv'
    ]
    
    missing_files = []
    existing_files = []
    for relative_path in expected_files:
        full_path = os.path.join(project_root, relative_path)
        if not os.path.exists(full_path):
            missing_files.append(relative_path)
        else:
            existing_files.append(relative_path)
            
    earned = int(round(10.0 * len(existing_files) / len(expected_files)))
    request.node._earned_points = earned
    
    assert len(missing_files) == 0, f"Missing required files/datasets under project directory: {missing_files}"
    print("All core files and datasets present!")

@pytest.mark.weight(30)
@pytest.mark.number("1.2")
def test_scheduler_generates_timetable(request):
    """Test that studentscheduler() in app.py executes and generates <studentid>_timetable.csv"""
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
        
    try:
        import app
    except ImportError as e:
        pytest.fail(f"Could not import app.py: {e}")
        
    if not hasattr(app, 'studentscheduler') or not callable(getattr(app, 'studentscheduler')):
        pytest.fail("app.py must define a callable function named 'studentscheduler()'")
        
    data_dir = os.path.join(project_root, 'data')
    output_dir = os.path.join(project_root, 'data')
    
    # Run the student scheduler
    try:
        result = app.studentscheduler(data_dir=data_dir, output_dir=output_dir)
    except Exception as e:
        pytest.fail(f"studentscheduler() failed during execution with error: {e}")
        
    # Check if timetable CSV exists
    # First check returned path if valid string
    csv_file = None
    if isinstance(result, str) and os.path.exists(result) and result.endswith('.csv'):
        csv_file = result
    else:
        # Check in output_dir for any *_timetable.csv
        matching = glob.glob(os.path.join(output_dir, "*_timetable.csv"))
        if not matching:
            # Check project root as fallback
            matching = glob.glob(os.path.join(project_root, "*_timetable.csv"))
        if matching:
            csv_file = matching[0]
            
    assert csv_file is not None and os.path.exists(csv_file), (
        "studentscheduler() did not generate any '<studentid>_timetable.csv' file in data/ folder. "
        f"Return value was: {result}"
    )
    
    # Check that the file is not empty
    file_size = os.path.getsize(csv_file)
    assert file_size > 0, f"Generated timetable CSV '{os.path.basename(csv_file)}' is empty (0 bytes)"
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
        
    assert len(lines) >= 2, (
        f"Generated timetable CSV '{os.path.basename(csv_file)}' should contain a header and scheduled course rows (found {len(lines)} lines)"
    )
    
    print(f"Successfully verified generated timetable CSV: {csv_file} ({len(lines)} lines)")
