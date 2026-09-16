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
        result = extract_skills("I know JavaScript.", ["Java"])
        self.assertEqual(result, [])

    def test_extract_skills_ignores_case(self):
        result = extract_skills("PYTHON, sql and git.", SKILLS)
        self.assertEqual(result, ["Python", "SQL", "Git"])

    def test_compare_skills(self):
        resume_skills = ["Python", "SQL", "Git"]
        job_skills = ["Python", "Java", "SQL", "Linux"]
        matching_skills, missing_skills = compare_skills(resume_skills, job_skills)
        self.assertEqual(matching_skills, ["Python", "SQL"])
        self.assertEqual(missing_skills, ["Java", "Linux"])

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
