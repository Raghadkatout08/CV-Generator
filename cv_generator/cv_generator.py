import sys

try:
    with open('assests/cv_template.txt', 'r') as file:
        file_read = file.read()
        print(file_read)

except FileNotFoundError:
    print("Error: CV Templete File Not Found")
    sys.exit(1)

except IOError:
    print("Error: Unable to read CV template file.")
    sys.exit(1)

print("Welcome to the CV Generator!")
print("Please Provide the following information to generate your CV.")


try:
    user_input = {}

    user_input['Name'] = input("Enter your name : ")
    user_input['phone_number'] = input("Enter your phone number : ")
    user_input['email'] = input("Enter your email : ")
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

except KeyboardInterrupt:
    print("\n CV Generation Interruped.")
    sys.exit(1)



cv_info = file_read.format(**user_input)

print("\n Your Info: ")
print(cv_info)

try:

    with open('assests/update_CV.txt' , 'w') as output_file:
        output_file.write(cv_info)
    print("Your CV has been generated and saved to 'assets/update_CV.txt'.")

except IOError:
    print("Error: Inable to write CV to file.")
    sys.exit(1)