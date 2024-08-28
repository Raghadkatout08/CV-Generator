import pytest
from cv_generator.cv_generator import read_template, parse_template, merge

def test_read_template_returns_stripped_string():
    """
    Test that the `read_template` function correctly reads and strips the content of a file.
    """
    actual = read_template("./assets/personal_summary.txt")
    expected = "I'm {Name} and I have Bachelor's degree in {major} and Currently working as a {job_title}  -  at {company_name}."
    assert actual == expected

def test_parse_template():
    """
    Test that `parse_template` correctly parses the template string into cleaned template and placeholders.
    """
    template = "I'm {Name} and I have Bachelor's degree in {major} and Currently working as a {job_title}  -  at {company_name}."
    actual_stripped, actual_parts = parse_template(template)
    expected_stripped = "I'm {} and I have Bachelor's degree in {} and Currently working as a {}  -  at {}."
    expected_parts = ("Name", "major", "job_title", "company_name")
    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts

def test_merge():
    """
    Test that `merge` correctly replaces placeholders in the template with provided values.
    """
    template = "I'm {} and I have Bachelor's degree in {} and Currently working as a {}  -  at {}."
    placeholders = ("john", "CS", "developer", "ABCIT")
    actual = merge(template, placeholders)
    expected = "I'm john and I have Bachelor's degree in CS and Currently working as a developer  -  at ABCIT."
    assert actual == expected

def test_read_template_raises_exception_with_bad_path():
    """
    Test that `read_template` raises a FileNotFoundError when given a non-existent file path.
    """
    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)
