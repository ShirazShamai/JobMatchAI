import unittest

from matcher import (
    extract_skills,
    compare_skills,
    calculate_match_score,
    generate_suggestions,
)
from skills import SKILLS


class TestMatcher(unittest.TestCase):
    def test_extract_skills(self):
        text = "I know Python, SQL and Git."
        result = extract_skills(text, SKILLS)
        self.assertEqual(result, ["Python", "SQL", "Git"])

    def test_javascript_is_not_java(self):
        result = extract_skills("I know JavaScript.", SKILLS)
        self.assertEqual(result, ["JavaScript"])

    def test_extract_skills_ignores_case(self):
        result = extract_skills("PYTHON, sql and git.", SKILLS)
        self.assertEqual(result, ["Python", "SQL", "Git"])

    def test_extract_multiword_skills(self):
        text = "Experience with REST API and Machine Learning."
        result = extract_skills(text, SKILLS)
        self.assertEqual(result, ["REST API", "Machine Learning"])

    def test_multiword_skills_ignore_case_and_extra_whitespace(self):
        text = "rest   api and MACHINE\nLEARNING"
        result = extract_skills(text, ["REST API", "Machine Learning"])
        self.assertEqual(result, ["REST API", "Machine Learning"])

    def test_multiword_skills_require_whole_consecutive_words(self):
        text = "REST APIs, Machine LearningTools, Machine and Learning"
        result = extract_skills(text, ["REST API", "Machine Learning"])
        self.assertEqual(result, [])

    def test_extract_skills_with_special_characters(self):
        result = extract_skills("I know (C++), [C#].", SKILLS)
        self.assertEqual(result, ["C++", "C#"])

    def test_similar_skill_names_are_not_confused(self):
        result = extract_skills("GitHub, MySQL, PostgreSQL and daily work.", SKILLS)
        self.assertEqual(result, ["MySQL", "PostgreSQL", "GitHub"])

    def test_repeated_skill_is_returned_once(self):
        result = extract_skills("Machine Learning and machine learning", SKILLS)
        self.assertEqual(result, ["Machine Learning"])

    def test_short_skill_remains_when_longer_skill_is_not_found(self):
        result = extract_skills("Experience with REST.", SKILLS)
        self.assertEqual(result, ["REST"])

    def test_longer_skill_is_preferred_regardless_of_list_order(self):
        result = extract_skills("rest api", ["REST API", "REST"])
        self.assertEqual(result, ["REST API"])

    def test_separate_similar_words_are_kept(self):
        result = extract_skills("Java and JavaScript, Git and GitHub", SKILLS)
        self.assertEqual(result, ["Java", "JavaScript", "Git", "GitHub"])

    def test_only_most_specific_skill_is_kept(self):
        skills = ["Learning", "Machine Learning", "Machine Learning Engineer"]
        result = extract_skills("Machine Learning Engineer", skills)
        self.assertEqual(result, ["Machine Learning Engineer"])

    def test_compare_skills(self):
        resume_skills = ["Python", "SQL", "Git"]
        job_skills = ["Python", "Java", "SQL", "Linux"]
        matching_skills, missing_skills, extra_skills = compare_skills(resume_skills, job_skills)
        self.assertEqual(matching_skills, ["Python", "SQL"])
        self.assertEqual(missing_skills, ["Java", "Linux"])
        self.assertEqual(extra_skills, ["Git"])

    def test_calculate_match_score(self):
        matching_skills = ["Python", "SQL"]
        job_skills = ["Python", "Java", "SQL", "Linux"]
        score = calculate_match_score(matching_skills, job_skills)
        self.assertEqual(score, 50.0)

    def test_match_score_with_empty_job_skills(self):
        score = calculate_match_score([], [])
        self.assertEqual(score, 0)

    def test_generate_suggestions(self):
        result = generate_suggestions(["Java", "Linux"])
        expected = ["Consider learning or highlighting experience with: Java, Linux."]
        self.assertEqual(result, expected)

    def test_generate_suggestions_without_missing_skills(self):
        result = generate_suggestions([])
        self.assertEqual(result, ["Great! No missing skills were found."])


if __name__ == "__main__":
    unittest.main()
