from matcher import extract_skills, compare_skills, calculate_match_score
from skills import SKILLS

resume_text = "I know Python, SQL and Git."
job_text = "We are looking for Python, Java, SQL and Linux."

resume_skills = extract_skills(resume_text, SKILLS)
job_skills = extract_skills(job_text, SKILLS)

matching_skills, missing_skills, extra_skills = compare_skills(resume_skills, job_skills)
match_score = calculate_match_score(matching_skills, job_skills)

print("resume_skills:", resume_skills)
print("job_skills:", job_skills)
print("matching_skills:", matching_skills)
print("missing_skills:", missing_skills)
print("extra_skills:", extra_skills)
print("match_score:", match_score)
