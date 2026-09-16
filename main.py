from matcher import extract_skills, compare_skills, calculate_match_score
from skills import SKILLS

resume_text = input("Enter your resume text: ")
job_text = input("Enter the job description: ")

resume_skills = extract_skills(resume_text, SKILLS)
job_skills = extract_skills(job_text, SKILLS)

matching_skills, missing_skills = compare_skills(resume_skills, job_skills)
match_score = calculate_match_score(matching_skills, job_skills)

print("Skills on resume:", resume_skills)
print("Skills for the job:", job_skills)
print("Matching skills", matching_skills)
print("Missing skills:", missing_skills)
print("Match score", f"{match_score:.2f}", "%")
