import random

# Generate a unique visit ID for each session
student_Id = random.randint(1000, 9999)

print("Welcome To Ulster University")
print("You can clock in with this system")
print("Visit ID:", student_Id)

student_or_visitor = input("Are you a visitor or a Student? ").strip().lower()

if student_or_visitor == "student":
    
 # STUDENT MENU
    while True:
        student_number_input = input("Kindly input your student registration number: ").strip()
        if student_number_input.isdigit():
            student_number = int(student_number_input)
            break
        else:
            print("Please enter a valid numeric registration number.")

    if student_number >= 100:
        print("Dear Student, Welcome to school, we hope you enjoy learning today and please always reach-out to the student support for enquiries")
        full_name = input("Kindly type your full name: ")
        course = input("What is your course of study: ")
        print("Thank you,", full_name + "! You have been checked in successfully.")

    else:
        print("This student number does not exist")
        
# VISITOR'S MENU
else:
    print("Welcome to our esteemed institution")
    visitor_name = input("Please input your full name: ")

    Lecturers_list = ["Dr James", "Dr Emeka", "Prof Thomas"]

    print("Please who is hosting you? Choose from the list:")
    for i, lecturer in enumerate(Lecturers_list, start=1):
        print(i, "-", lecturer)

    while True:
        choice = input("Enter the number of your host: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(Lecturers_list):
            selected_lecturer = Lecturers_list[int(choice) - 1]
            break
        else:
            print("Please enter a valid number from the list.")

    if selected_lecturer == "Dr James":
        print("Dear Visitor, please be informed that Dr James is currently unavailable. Kindly contact him or reschedule your appointment.")
    elif selected_lecturer == "Dr Emeka":
        print("You can walk to his office, he is available.")
    elif selected_lecturer == "Prof Thomas":
        print("Prof Thomas has just embarked on a 20-day work leave. Please contact him to reschedule.")
