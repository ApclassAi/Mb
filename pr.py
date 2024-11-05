import random

# -------------1-------------
studentList = ["Jafar", "Hashem", "Ali"]

def add_new_student():
    while True:
        student_name = input("Enter Student's Name (Enter 0 to Finish): ")
        if student_name == "0":
            print("Updated Student List:", studentList)
            break
        else:
            studentList.append(student_name)

# -------------2-------------
def check_random_number():
    random_numbers = [random.randint(0, 10) for _ in range(5)]
    user_input = int(input("Enter a Number between 0 and 10: "))
    match_found = user_input in random_numbers
    print("Generated Numbers:", random_numbers)
    print("Match Found:", match_found)

# -------------3-------------
def reverse_list():
    user_list = []
    while True:
        item = input("Enter List Value (Enter 0 to Finish): ")
        if item == "0":
            reversed_list = user_list[::-1]
            print("Original List:", user_list)
            print("Reversed List:", reversed_list)
            break
        else:
            user_list.append(item)

# -------------4-------------
def remove_student():
    students = ["Mohammad", "Javad", "Mahdi", "Ali", "Reza", "Seyed"]
    student_to_remove = input("Enter Student Name to Remove: ")
    if student_to_remove in students:
        students.remove(student_to_remove)
        print("Updated Student List:", students)
    else:
        print("Student Not Found.")

# -------------5-------------
def merge_lists():
    list1, list2 = [], []
    while True:
        item1 = input("Enter Value for List 1 (Enter 0 to Finish): ")
        if item1 == "0":
            while True:
                item2 = input("Enter Value for List 2 (Enter 0 to Finish): ")
                if item2 == "0":
                    merged_list = list1 + list2
                    print("List 1:", list1)
                    print("List 2:", list2)
                    print("Merged List:", merged_list)
                    break
                else:
                    list2.append(item2)
            break
        else:
            list1.append(item1)

# -------------1-------------
def favorite_colors():
    colors = []
    while True:
        color = input("Enter Your Favorite Color (Enter 0 to Finish): ")
        if color == "0":
            color_tuple = tuple(colors)
            print("Favorite Colors:", color_tuple)
            break
        else:
            colors.append(color)

# -------------2-------------
def count_occurrences():
    numbers = (1, 2, 3, 4, 5, 6, 5, 7, 8, 9, 10)
    num = int(input("Enter a Number to Check Count: "))
    print(f"{num} occurs {numbers.count(num)} times in the tuple.")

# -------------3-------------
def find_month():
    months = ("Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Dey", "Bahman", "Esfand")
    month_input = input("Enter Month: ")
    if month_input in months:
        print("Month Found in the List.")
    else:
        print("Month Not Found.")

# -------------4-------------
def calculate_average_score():
    scores = (("Mahdi", 16), ("Ali", 16), ("Mohammad", 16))
    for student, score in scores:
        print(f"{student}: {score}")

# -------------1-------------
def check_even_odd():
    num = int(input("Enter a Number: "))
    if num % 2 == 0:
        print("The Number is Even.")
    else:
        print("The Number is Odd.")

# -------------2-------------
def room_temperature():
    temperature = int(input("Enter Room Temperature: "))
    if temperature > 15:
        print("Your Room is Hot.")
    else:
        print("Your Room is Cold.")

# -------------3-------------
def login_system():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == "User" and password == "1234":
        print("Login Successful!")
    else:
        print("Invalid Username or Password.")

# -------------4-------------
def check_voting_eligibility():
    citizenship = input("Are You a Citizen of IRAN (YES or NO): ").lower()
    age = int(input("Enter Your Age: "))
    if citizenship == "yes" and age >= 18:
        print("You Are Eligible to Vote.")
    elif citizenship == "yes":
        print("You Are Too Young to Vote.")
    else:
        print("You Are Not a Citizen of IRAN.")

# -------------5-------------
def check_offer_eligibility():
    is_user = input("Are You a Registered User (yes or no): ").lower()
    money_spent = int(input("Enter Your Spending Amount ($): "))
    if is_user == "yes" and money_spent >= 100:
        print("You Are Eligible for the Offer.")
    else:
        print("You Are Not Eligible for the Offer.")

# -------------1-------------
def print_numbers():
    for num in range(1, 101):
        print(num)

# -------------2-------------
def sum_numbers():
    total = sum(range(1, 51))
    print("Sum of Numbers from 1 to 50:", total)

# -------------3-------------
def multiplication_table():
    number = int(input("Enter a Number for Multiplication Table: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# -------------4-------------
def calculate_factorial():
    number = int(input("Enter a Number to Calculate Factorial: "))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"Factorial of {number}: {factorial}")

# -------------5-------------
def sum_even_numbers():
    even_sum = sum(x for x in range(1, 101) if x % 2 == 0)
    print("Sum of Even Numbers from 1 to 100:", even_sum)

# منوی اصلی
while True:
    print("[1] List Operations\n[2] Tuple Operations\n[3] If Conditions\n[4] For Loops\n[0] Exit")
    choice = input("Choose an Option: ")
    
    if choice == "1":
        while True:
            print("[1] Add New Student\n[2] Check Random Number\n[3] Reverse List\n[4] Remove Student\n[5] Merge Lists\n[0] Back to Main Menu")
            option = input("Choose an Option: ")
            if option == "1":
                add_new_student()
            elif option == "2":
                check_random_number()
            elif option == "3":
                reverse_list()
            elif option == "4":
                remove_student()
            elif option == "5":
                merge_lists()
            elif option == "0":
                break

    elif choice == "2":
        while True:
            print("[1] Favorite Colors\n[2] Count Occurrences\n[3] Find Month\n[4] Calculate Average Score\n[0] Back to Main Menu")
            option = input("Choose an Option: ")
            if option == "1":
                favorite_colors()
            elif option == "2":
                count_occurrences()
            elif option == "3":
                find_month()
            elif option == "4":
                calculate_average_score()
            elif option == "0":
                break

    elif choice == "3":
        while True:
            print("[1] Check Even or Odd\n[2] Room Temperature\n[3] Login System\n[4] Voting Eligibility\n[5] Offer Eligibility\n[0] Back to Main Menu")
            option = input("Choose an Option: ")
            if option == "1":
                check_even_odd()
            elif option == "2":
                room_temperature()
            elif option == "3":
                login_system()
            elif option == "4":
                check_voting_eligibility()
            elif option == "5":
                check_offer_eligibility()
            elif option == "0":
                break

    elif choice == "4":
        while True:
            print("[1] Print Numbers 1-100\n[2] Sum Numbers 1-50\n[3] Multiplication Table\n[4] Calculate Factorial\n[5] Sum Even Numbers 1-100\n[0] Back to Main Menu")
            option = input("Choose an Option: ")
            if option == "1":
                print_numbers()
            elif option == "2":
                sum_numbers()
            elif option == "3":
                multiplication_table()
            elif option == "4":
                calculate_factorial()
            elif option == "5":
                sum_even_numbers()
            elif option == "0":
                break

    elif choice == "0":
        print("Exiting Program...")
        break
