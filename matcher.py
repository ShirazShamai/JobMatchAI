def extract_skills(text, skills):
    text = text.lower()

    for punctuation in ",.;:()[]":
        text = text.replace(punctuation, " ")

    words = text.split()
    normalized_text = " " + " ".join(words) + " "
    found_skills = []

    for skill in skills:
        # ?????? ???? ?????? ?????? ????? ???? ???? ????.
        skill_text = " " + skill.lower() + " "
        if skill_text in normalized_text:
            found_skills.append(skill)

    specific_skills = []

    for skill in found_skills:
        is_part_of_longer_skill = False
        skill_text = " " + skill.lower() + " "

        for other_skill in found_skills:
            other_skill_text = " " + other_skill.lower() + " "
            if len(other_skill) > len(skill) and skill_text in other_skill_text:
                is_part_of_longer_skill = True
                break

        if not is_part_of_longer_skill:
            specific_skills.append(skill)

    return specific_skills


def compare_skills(resume_skills, job_skills):
    matching_skills = []
    missing_skills = []
    extra_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)

    for skill in resume_skills:
        if skill not in job_skills:
            extra_skills.append(skill)

    return matching_skills, missing_skills, extra_skills


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
