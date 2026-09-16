# JobMatchAI

JobMatchAI is a simple Python application that compares a resume PDF with a job description. It offers both a tkinter desktop GUI and a terminal version, showing skill matches, gaps, a match score, and suggestions.

The current version uses predefined skills and text matching, without an AI API.

## Features

- Extract resume text from all pages of a PDF.
- Choose a PDF in the GUI and paste a job description into a multiline text field.
- View a prominent match score, organized skill lists, and a separate suggestions area.
- Identify matching skills (in both texts), missing skills (only in the job description), and extra skills (only in the resume).
- Display the match score with two decimal places and suggestions based on missing skills.
- Reset the selected PDF, job description, and results with the **Clear** button.
- Show friendly GUI error messages for missing input, missing or unreadable PDFs, and PDFs without extractable text.
- Detect skills regardless of letter case, including multi-word skills such as REST API and Machine Learning.
- Prefer a more specific detected skill, such as REST API over REST, and avoid detecting Java inside JavaScript.
- Run the same matching functions through the terminal.

## Technologies

- **Python**: application logic.
- **tkinter / ttk**: desktop interface and styled widgets.
- **pypdf**: PDF text extraction.
- **unittest**: automated unit tests.
- **Git/GitHub**: version control and repository hosting.

## Installation

Install Python with tkinter support, then install the dependencies from the project folder:

```bash
python -m pip install -r requirements.txt
```

## Running the Application

Run either version from the project folder.

### Desktop GUI

```bash
python gui.py
```

Click **Choose Resume PDF**, paste the job description, and click **Analyze**. Inputs appear on the left and results on the right. Click **Clear** to reset the form.

### Terminal

```bash
python main.py
```

Enter the PDF path (with or without surrounding quotes), then enter the job description on one line and press Enter.

## Screenshot

*GUI screenshot coming soon.*

<!-- Add the image when available: ![JobMatchAI GUI](docs/screenshot.png) -->

## Running Tests

```bash
python -m unittest tests.py
```

The unit tests cover skill extraction, multi-word skills, preference for more specific skills, skill comparison, score calculation, and suggestions.

## Example Output

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

The score is `(number of matching skills / number of detected job skills) * 100`. If no job skills are detected, it is 0. This measures detected skill overlap, not overall suitability for a role.

## Current Limitations

- Skill detection relies on the predefined list in skills.py.
- Matching does not understand context, experience levels, or synonyms.
- PDFs must contain extractable text; image-only scans are not supported.
- The terminal version accepts a single-line job description; the GUI supports multiple lines.
- There is no AI API integration.

## Future Improvements

- Web interface.
- AI-based semantic matching.
- Load job descriptions from a file or URL.
- Broader skill coverage and support for synonyms.
