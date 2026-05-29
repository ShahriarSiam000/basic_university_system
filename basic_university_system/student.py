class student:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

    def grade(self, total_marks):
        if total_marks >= 80:
            return 4.00
        elif total_marks >= 75:
            return 3.75
        elif total_marks >= 70:
            return 3.50
        elif total_marks >= 65:
            return 3.25
        elif total_marks >= 60:
            return 3.00
        elif total_marks >= 55:
            return 2.75
        elif total_marks >= 50:
            return 2.50
        elif total_marks >= 45:
            return 2.25
        elif total_marks >= 40:
            return 2.00
        else:
            return 0.00
        
    def display_info(self):
        print (f"----------------------")
        print(f"your name is {self.name}")
        print(f"your ID is {self.id}")
        print(f"your Department is {self.department}")
        