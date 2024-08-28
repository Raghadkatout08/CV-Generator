import re

def read_template(file_path):
    """
    Reads the content of a file and returns it as a string.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file as a string.

    Raises:
        FileNotFoundError: If the specified file_path does not exist.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")

def create_profile():
    """
    Create a profile tuple based on user input.

    Returns:
        tuple: A tuple containing the profile information.
    """
    name = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    city = input("Enter your city: ")
    university_name = input("Enter your university name: ")
    major = input("Enter your major: ")
    graduation_date = input("Enter your graduation date: ")
    company_name = input("Enter your company name: ")
    job_title = input("Enter your job title: ")
    responsibilities = input("Enter your job responsibilities: ")
    skill_1 = input("Enter your skill_1: ")
    skill_2 = input("Enter your skill_2: ")
    skill_3 = input("Enter your skill_3: ")
    skill_4 = input("Enter your skill_4: ")
    arabic_language_level = input("Enter Arabic language level: ")
    english_language_level = input("Enter English language level: ")

    profile = [
        name, phone_number, email, city, university_name, major, graduation_date,
        company_name, job_title, responsibilities, skill_1, skill_2, skill_3, skill_4,
        arabic_language_level, english_language_level
    ]
    
    return tuple(profile)

def parse_template(template):
    """
    Parse a template string and separate the placeholder parts.

    Args:
        template (str): The template string with placeholders.

    Returns:
        tuple: Contains:
            - cleaned_template (str): The template string with placeholders replaced by '{}'.
            - placeholders (tuple): Tuple containing the placeholder parts.
    """
    placeholder_pattern = r'{([^}]*)}'
    placeholders = re.findall(placeholder_pattern, template)
    cleaned_template = re.sub(placeholder_pattern, '{}', template)
    return cleaned_template.strip(), tuple(placeholders)

def merge(template, placeholders):
    """
    Merge a template string with a tuple of placeholder values.

    Args:
        template (str): The template string with curly braces as placeholders.
        placeholders (tuple): Tuple containing the placeholder values.

    Returns:
        str: The merged string with placeholders replaced by corresponding values.
    """
    for placeholder in placeholders:
        template = template.replace('{}', str(placeholder), 1)
    return template

if __name__ == "__main__":
    print("Welcome to CV Generator!\n")
    print("This project provides a script to generate a CV (Curriculum Vitae) based on a template file and user input.")
    print("It allows users to create personalized CVs quickly and easily.\n")

    path = "./assets/cv_template.txt"
    content = read_template(path)
    template, placeholders = parse_template(content)
    user_input = create_profile()
    cv = merge(template, user_input)

    try:
        with open("./assets/cv_output.txt", "w") as file:
            file.write(cv)
        print("CV generated successfully. Check the 'cv_output.txt' file.")
    except Exception as e:
        print(f"An error occurred while writing the CV: {e}")