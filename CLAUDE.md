# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Note**: Additional user preferences and learning context are available in `.claude/instructions.md`.

## Coaching-Focused Approach

All Claude Code assistance in this repository is centered around **coaching and feedback** rather than direct code provision. This means:

- **Primary response**: Guidance, explanations, and helping understand problems
- **Secondary response**: Code examples only when coaching isn't sufficient
- Focus on understanding the "why" behind concepts and best practices
- Emphasis on developing problem-solving skills and Python thinking patterns

## Repository Overview

This is a Python learning repository containing code from the "100 Days of Code Complete Professional Python Bootcamp" by App Brewery. The repository is structured as a progressive learning journey from beginner to advanced Python concepts.

## Repository Structure

The codebase is organized into learning phases:

- `beginner/`: Days 1-15 - Python fundamentals (variables, control flow, functions, data structures)
- `intermediate/`: Days 16-31 - OOP and external libraries  
- `intermediate-plus/`: Days 32-58 - APIs, web scraping, Flask (planned)
- `advanced/`: Days 59-81 - Data science and analysis (planned)
- `portfolio-projects/`: Days 82-100 - Professional portfolio builds (planned)
- `course-code-examples/`: Official course reference materials and solutions
- `course-documents/`: Course syllabus and reference PDFs

## Development Workflow

### Running Python Files

All Python files can be executed directly:
```bash
python3 beginner/day_1_task.py
python3 intermediate/day15/task.py
```

### File Naming Conventions

**Beginner section (legacy structure):**
- `day_X_task.py`: Main project/exercise for day X
- `day_X_notes.py`: Learning notes and examples for day X  
- `day_X_art.py`: ASCII art or visual elements used in projects
- `day_X_*.py`: Additional files for specific concepts (e.g., `day_8_task_modulo.py`)

**Intermediate onwards (modular structure):**
- `dayX/`: Directory for each day's work
- `dayX/task.py`: Main project/exercise file
- `dayX/data.py`: Data constants and configuration
- `dayX/*.py`: Additional modules as needed for the project

### Code Organization Patterns

Each day typically contains:
- Detailed docstrings explaining the project requirements
- Helper functions with descriptive names
- Error handling using try/except blocks for user input
- Clear separation between data and logic (e.g., importing from `data.py`)
- From intermediate onwards: modular structure with separate directories for easier imports and module references

### Testing

No formal testing framework is used. Code validation is done through:
- Manual execution and testing of each script
- Following the specific requirements outlined in docstrings
- Comparing outputs with course examples when available

## Key Technologies

- **Python 3**: Core language
- **Standard Library**: Primary focus on built-in modules (random, math, etc.)
- **External Libraries**: Introduced progressively (currently none in beginner section)

## Learning Progress Tracking

The current branch `intermediate` indicates active work on the intermediate section. Progress can be tracked through:
- Completed files in each directory
- Git commit history following the pattern "Complete Day X" or "Day X Complete"
- README.md progress checklist

## Important Notes

- This is a learning repository - code style prioritizes clarity and educational value over production optimization
- Each day builds incrementally on previous concepts
- Solutions include detailed comments explaining logic and requirements
- Error handling is implemented for user input validation