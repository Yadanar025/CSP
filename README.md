## Project Overview: University Class Scheduling & Timetable Optimizer

In this assignment, you will model and implement an automated intelligent class scheduling system for a university academic department. You will formulate the scheduling problem as a Constraint Satisfaction Problem (CSP), enforce hard constraints, optimize soft constraints using heuristics and metaheuristics, and generate an academic timetable exported as `<studentid>_timetable.csv`.

The datasets are provided in the `data/` directory. You will implement the main entry point `studentscheduler()` inside `app.py`. You have full freedom in how you organize your internal classes, modules, and folder structure.

### Learning Objectives

1. **CSP Formulation:** Formulate a real-world scheduling problem into Variables ($X$), Domains ($D$), and Hard/Soft Constraints ($C$).
2. **Constraint Engine & Validation:** Model and enforce hard constraints (zero double-bookings, room capacity limits, instructor availability, cohort clash prevention) and calculate soft constraint penalty scores.
3. **Heuristic CSP Search:** Implement CSP Backtracking enhanced with Minimum Remaining Values (MRV), Degree Heuristic, Least Constraining Value (LCV), and Forward Checking.
4. **Local Search & Metaheuristics:** Implement Min-Conflicts and local search (Simulated Annealing or Genetic Algorithm) for soft constraint optimization.
5. **Dynamic Timetable Export:** Read relational datasets dynamically and export the generated schedule to `<studentid>_timetable.csv`.

---

## Submission Guidelines

To submit your project, please ensure you complete all required tasks and follow these instructions carefully.

### 1. Preparation Checklist
Before pushing your final submission, verify that:
*   [ ] You have implemented your scheduler in or called from `studentscheduler()` in `app.py`.
*   [ ] Running `studentscheduler()` dynamically reads from `data/` and generates `<studentid>_timetable.csv` in `data/`.
*   [ ] Your code works dynamically when datasets are updated.
*   [ ] You have completed the AI Student Declaration on [PETRA AI](https://www.petraai.org/student) and saved it as `AI_declaration.png` in the repository root.
*   [ ] You have completed all sections in `report.md` (with your Name, MMDT ID, video presentation link, directory structure explanation, and discussion). Do not alter the structure of `report.md`.
*   [ ] You have recorded a 5–7 minute video presentation (.mp4, face visible) explaining your project directory structure, problem formulation, and demonstration of `studentscheduler()`, and uploaded it to YouTube, Google Drive, or Dropbox (with public view access).

### 2. How to Submit
Once everything is ready, commit and push your code to your GitHub repository's `main` or `master` branch:
```bash
git add .
git commit -m "Submit Project 2: University Class Scheduling"
git push origin main
```
The automated autograding system will automatically run tests upon pushing to the `main` or `master` branch.

---

## Checking Grades

You can check your project grades both locally and online via GitHub Actions.

### 1. Locally (Before Submitting)
You can run the autograding tests on your local machine:
1. Make sure you have installed the dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
2. Run `pytest` inside the project root:
   ```bash
   pytest tests/
   ```
3. A scorecard summarizing your earned marks will be outputted directly in the terminal under the section **"AUTOGRADING SCORECARD"**.

### 2. On GitHub (After Submitting)
Every push to the repository triggers the online autograder.
1. Go to the **Actions** tab of your GitHub repository.
2. Select the latest run (e.g., "Autograder Check" or your commit message).
3. Under the run details, scroll to the bottom or open the job logs to view the **Autograding Scorecard** step summary, which details your score out of 70 marks.

### 3. Grading Details & Passing Requirements
*   **Total Score:** 70 marks (40 marks for implementation and timetable CSV generation, 30 marks for report/video presentation).
*   **Passing Score:** **70 marks**.
*   **Deadline:** **September 20, 2026, at 23:59:59**.
*   **Late Submission Policy:** A penalty of **-10 marks per day** will be applied for late submissions.
*   **Commitment Fee:** Any late, missing, or failed project (score < 70%) will carry a **30,000 MMK commitment fee**, calculated and collected at the end of the 10-week challenge.
