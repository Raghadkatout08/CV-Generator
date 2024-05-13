# test_cv_generator.py

import pytest
from cv_generator import read_template, parse_template, merge

def test_read_template_returns_stripped_string():
    actual = read_template("assets/personal_summary.txt")
    expected = "I'm {Name} and I have Bachelor's degree in {major} and Currently working as a {job_title}  -  at {company_name}."
    assert actual == expected

def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "I'm {Name} and I have Bachelor's degree in {major} and Currently working as a {job_title}  -  at {company_name}."
    )
    expected_stripped = "I'm {} and I have Bachelor's degree in {} and Currently working as a {}  -  at {}."
    expected_parts = (
        "Name",
        "major",
        "job_title",
        "company_name",
    )

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

def test_merge():
    actual = merge(
        "I'm {} and I have Bachelor's degree in {} and Currently working as a {}  -  at {}.",
        ("John", "Computer Science", "Software Developer", "XYZ Corp"),
    )
    expected = "I'm John and I have Bachelor's degree in Computer Science and Currently working as a Software Developer  -  at XYZ Corp."
    assert actual == expected

def test_read_template_raises_exception_with_bad_path():
    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)
