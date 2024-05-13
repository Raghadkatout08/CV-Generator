with open('assests/cv_template.txt', 'r') as file:
    file_read = file.read()
    print(file_read)

user_input = {}

user_input['Name'] = input("Enter your name : ")
user_input['phone_number'] = input("Enter your phone number : ")
user_input['city'] = input("Enter your city : ")
user_input['university_name'] = input("Enter your university name : ")
user_input['major'] = input("Enter your university major : ")
user_input['graduation_date'] = input("Enter your graduation date : ")
user_input['company_name'] = input("Enter your company_name : ")
user_input['job_title'] = input("Enter your job_title : ")
user_input['you_responsibilities'] = input("Enter your you_responsibilities : ")
user_input['skill-01'] = input("Enter your skill 1: ")
user_input['skill-02'] = input("Enter your skill 2: ")
user_input['skill-03'] = input("Enter your skill 3: ")
user_input['skill-04'] = input("Enter your skill 4: ")
user_input['Arabic_language_level'] = input("Enter your Arabic_language_level : ")
user_input['English_language_level'] = input("Enter your English_language_level : ")

print(user_input)
