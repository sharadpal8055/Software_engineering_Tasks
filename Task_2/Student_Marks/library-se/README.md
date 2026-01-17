# Student Marks Management System

A backend-focused Student Marks Management System built using Python,
demonstrating **Agile development**, **Test-Driven Development (TDD)**,
and **Git-based engineering workflows**.

This project emphasizes **software engineering practices**, not just
feature implementation.

---

## Why this project?

Most student projects focus only on “making it work”.
This project focuses on **how software should be built in real teams**:

- Requirements broken into **incremental sprints**
- Features developed using **TDD (tests first)**
- Clean Git history with **feature branches and tagged releases**
- Traceability from **user stories → code → tests → versions**

---

## Features

- Add students with validation
- Record and validate marks
- Calculate grades based on rules
- Generate a formatted student report
- Fully covered by automated unit tests

---

## Tech Stack

- **Language:** Python 3
- **Testing:** unittest (Test-Driven Development)
- **Version Control:** Git, GitHub
- **Development Approach:** Agile, Sprint-based workflow

---

## Project Structure
library-se/
├── src/
│ └── app.py # Core application logic
├── tests/
│ └── test_app.py # Unit tests (TDD)
├── docs/
│ ├── USER_STORIES.md
│ └── TRACEABILITY.md
└── README.md

---

## How to Run

From the project root:

```bash
cd Task_2/Student_Marks/library-se
python3 -m unittest discover -s tests -p "test_*.py" -v
All tests should pass successfully.

Agile Development Workflow

The project was developed in three sprints:

Sprint-1 (v0.1):

Student registration

Marks entry

Input validation

Sprint-2 (v0.2):

Grade calculation logic

Sprint-3 (v0.3):

Student report generation

Each sprint:

Used a separate feature branch

Was merged into main only after tests passed

Was tagged with a version (v0.1, v0.2, v0.3)

Testing Approach (TDD)

Tests were written before implementation

Edge cases and invalid inputs are explicitly tested

All features are covered by automated unit tests

This ensures:

Early bug detection

Safer refactoring

Predictable behavior

What This Project Demonstrates

Backend development fundamentals

Clean and maintainable Python code

Test-Driven Development mindset

Git branching, merging, and tagging

Agile sprint discipline

Requirement traceability

Limitations & Possible Extensions

Current limitations:

In-memory data storage

Single-user usage

No persistence layer

Possible extensions:

REST API using Flask or FastAPI

Database integration (SQLite/PostgreSQL)

Authentication and role-based access

Export reports to CSV or PDF

Repository

GitHub:
https://github.com/sharadpal8055/Software_engineering_Tasks
