from student import student
from file_handling import create_file_if_dont_exist, save_student, save_marks
from analytics import show_top_students, show_avarage_marks, show_failed_student
import pandas as pd

create_file_if_dont_exist("C:/Users/Shahriar Siam/Desktop/git practice/basic_university_system/data/students.csv", ["id", "name", "department"])

create_file_if_dont_exist("C:/Users/Shahriar Siam/Desktop/git practice/basic_university_system/data/marks.csv", ["id", "ct", "assignment", "final"])



while True:
    print("\n===== UNIVERSITY SYSTEM =====")

    print("1. Add Student")
    print("2. Add Marks")
    print("3. Show Top Students")
    print("4. Show Average Marks")
    print("5. Show Failed Students")
    print("6. show the total student data")
    print("7. Exit")


    choice = input("Enter choice: ")

    if choice == '1':
        try:
            id = float(input("student ID: "))
            name = input("Name:")
            department = input("Department: ")

            st = student(name, id, department)
            save_student(st)

        except Exception as e:
            print("error", e)

    elif choice =='2':
        try:
            id = float(input("ID: "))
            ct = float(input("CT: "))
            assignment = float(input("Assignment: "))
            final = float(input("Final: "))
            total = id+ct+assignment+final

            save_marks(id, ct, assignment, final, total)
            print("marks added successfuly")

        except ValueError:
            print("invalid input numbers.")

    elif choice == '3':
        show_top_students()

    elif choice == '4':
        show_avarage_marks()

    elif choice == '5':
        show_failed_student()

    elif choice == '6':
        try:
            df = pd.read_csv("C:/Users/Shahriar Siam/Desktop/git practice/basic_university_system/data/students.csv")
            print(df)
            df2 = pd.read_csv("C:/Users/Shahriar Siam/Desktop/git practice/basic_university_system/data/marks.csv")
            print(df2)
            merged = pd.merge(df, df2, on='id')

            merged.to_csv("C:/Users/Shahriar Siam/Desktop/git practice/basic_university_system/data/merged_students.csv", index= False)
            print(merged)

        except FileNotFoundError:
            print("file not found")

        except Exception as e:
            print("error", e)

    else :
        break