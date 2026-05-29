import csv
import os 

def create_file_if_dont_exist(file_name, header):
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)


def save_student(student):
    with open("C:/Users/Shahriar Siam/Desktop/git practice/basic_university_system/data/students.csv", "a", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([student.id , 
                         student.name,
                         student.department])
        
def save_marks(id, ct, assignment, final,total):
    total = ct + assignment + final
    with open("C:/Users/Shahriar Siam/Desktop/git practice/basic_university_system/data/marks.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id,
                         ct,
                         assignment,
                         final,
                         total])
        