# JobMatchAI

JobMatchAI is a simple Python command-line application that compares a resume with a job description. It identifies matching, missing, and extra skills, calculates a match score, and provides suggestions based on missing skills.

The current version uses predefined skills and simple text matching. It does not use an AI API.

## Features

- Read resume text from all pages of a PDF file.
- Enter a job description through the terminal.
- Detect skills without distinguishing between uppercase and lowercase letters.
- Identify matching skills: skills found in both the resume and the job description.
- Identify missing skills: skills found in the job description but not in the resume.
- Identify extra skills: skills found in the resume but not in the job description.
- Display a match score with two decimal places.
- Provide one suggestion listing missing skills, or a positive message when none are missing.
- Support multi-word skills such as REST API and Machine Learning.
- Prefer a more specific detected skill, such as REST API, over a shorter skill contained within it, such as REST.
- Match whole words, so Java is not detected inside JavaScript.

## Technologies

- **Python**: application logic and terminal input/output.
- **pypdf**: PDF text extraction.
- **unittest**: automated unit tests using Python's built-in testing library.
- **Git/GitHub**: version control and repository hosting.

## Installation

Install Python, then run the following command from the project folder:

```bash
python -m pip install pypdf
```

## Running the Application

From the project folder, run:

```bash
python main.py
```

1. Enter the path to your resume PDF. Paths with or without surrounding single or double quotes are accepted.
2. Enter the job description on one line and press Enter.
3. Review the results in the terminal.

## Running Tests

From the project folder, run:

```bash
python -m unittest tests.py
```

The tests cover skill extraction, multi-word skills, preference for more specific skills, skill comparison, score calculation, and suggestions.

## Example Output

For a resume containing Python, SQL, and Git, and a job description containing Python, Java, SQL, and Linux:

```text
=== JobMatchAI Results ===
Resume skills: Python, SQL, Git
Job skills: Python, Java, SQL, Linux
Matching skills: Python, SQL
Missing skills: Java, Linux
Extra skills: Git
Match score: 50.00%

Suggestions:
Consider learning or highlighting experience with: Java, Linux.
```

The score is calculated as:

```text
(number of matching skills / number of detected job skills) * 100
```

If no job skills are detected, the score is 0. The score measures overlap between detected skills, not overall suitability for the role.

## Current Limitations

- Skill detection relies on the predefined list in skills.py.
- Matching uses words and phrases; it does not understand context, experience levels, or synonyms.
- PDFs must contain extractable text. Image-only scanned PDFs are not supported; there is no OCR (text recognition from images).
- The job description must currently be entered on one line in the terminal.
- There is currently no GUI or AI API integration.

## Future Improvements

These ideas are not implemented yet:

- GUI / web interface.
- AI-based semantic matching to compare meaning and context.
- Load job descriptions from a file or URL.
- Broader skill coverage and better support for synonyms.
