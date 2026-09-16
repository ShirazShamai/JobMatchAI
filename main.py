from matcher import extract_skills, compare_skills, calculate_match_score, generate_suggestions
from skills import SKILLS
from pdf_reader import read_pdf_text

resume_pdf_path = input("Enter the path to your resume PDF: ").strip()
if resume_pdf_path.startswith('"') and resume_pdf_path.endswith('"'):
    resume_pdf_path = resume_pdf_path[1:-1]
elif resume_pdf_path.startswith("'") and resume_pdf_path.endswith("'"):
    resume_pdf_path = resume_pdf_path[1:-1]
resume_text = read_pdf_text(resume_pdf_path)
job_text = input("Enter the job description: ")

resume_skills = extract_skills(resume_text, SKILLS)
job_skills = extract_skills(job_text, SKILLS)

matching_skills, missing_skills = compare_skills(resume_skills, job_skills)
match_score = calculate_match_score(matching_skills, job_skills)
suggestions = generate_suggestions(missing_skills)

print("\n=== JobMatchAI Results ===")
print("Resume skills:", ", ".join(resume_skills) or "None")
print("Job skills:", ", ".join(job_skills) or "None")
print("Matching skills:", ", ".join(matching_skills) or "None")
print("Missing skills:", ", ".join(missing_skills) or "None")
print(f"Match score: {match_score:.2f}%")

print("\nSuggestions:")
for suggestion in suggestions:
    print(suggestion)
