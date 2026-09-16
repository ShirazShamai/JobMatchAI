def extract_skills(text, skills):
    text = text.lower()

    for punctuation in ",.;:()[]":
        text = text.replace(punctuation, " ")

    words = text.split()
    found_skills = []

    for skill in skills:
        if skill.lower() in words:
            found_skills.append(skill)

    return found_skills


def compare_skills(resume_skills, job_skills):
    matching_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matching_skills, missing_skills


def calculate_match_score(matching_skills, job_skills):
    if not job_skills:
        return 0

    score = len(matching_skills) / len(job_skills) * 100
    return score


def generate_suggestions(missing_skills):
    if not missing_skills:
        return ["Great! No missing skills were found."]

    skills_text = ", ".join(missing_skills)
    return [f"Consider learning or highlighting experience with: {skills_text}."]
