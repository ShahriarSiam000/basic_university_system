import pandas as pd
import numpy as np

def show_top_students():
    try:
        df = pd.read_csv("C:/Users/Shahriar Siam/Desktop/git practice/basic_university_system/data/marks.csv")
        top_students = df.sort_values(by= "total", ascending=False)

        print("\n top students: ")
        print(top_students.head())

    except FileNotFoundError:
        print("marks file not found")


def show_avarage_marks():
    try:
        df = pd.read_csv("C:/Users/Shahriar Siam/Desktop/git practice/basic_university_system/data/marks.csv")
        avarage = df["total"].mean()

        print(f"the avarage number is {avarage}")

    except FileNotFoundError:
        print("marks file not found")

def show_failed_student():
    try:
        df = pd.read_csv("C:/Users/Shahriar Siam/Desktop/git practice/basic_university_system/data/marks.csv")
        failed = df[df["total"] < 40]
        print("\n failed students")
        print(failed)

    except FileNotFoundError:
        print("mark file not found")


    