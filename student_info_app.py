import uuid

class Data:

    def generate_id(self):
        return str(uuid.uuid4()).replace('-', '')

    def __init__(self, name, birth, gender):
        self.name = name
        self.birth = birth
        self.gender = gender
        self.id = self.generate_id()

class App:

    def __init__(self):
        self.students_list = {}

    def add_student(self, name, birth, gender):
        student = Data(name, birth, gender)
        self.students_list[student.id] = student

    def show_full_list(self):
        print(f"Here's the full students list:\n")
        for student_id, student in self.students_list.items():
            print(f"ID: {student.id}")
            print(f"Name: {student.name}")
            print(f"Birth: {student.birth}")
            print(f"Gender: {student.gender}\n")

    def search_student(self, student_id):
        return self.students_list.get(student_id, None)

    def update_student(self, student_id, name = None, birth = None, gender = None):
        student = self.search_student(student_id)
        if student:
            if name:
                student.name = name
            if birth:
                student.birth = birth
            if gender:
                student.gender = gender
        else:
            print(f"Student not found")

    def delete_student(self, student_id):
        if student_id in self.students_list:
            del self.students_list[student_id]
            print(f"Successfully deleted student with ID: {student_id}")
        else:
            print(f"Student not found")

def main():
    student = App()

    while True:
        print("\nOptions: \n1. Search student \n2. Update student \n3. Display all students \n4. Exit")
        option = int(input("\nChoose an option (1 - 4): "))

        if option == 1:
            student_id = input("\nInsert your student ID: ")
            student.search_student(student_id)

        elif option == 2:
            print("\nWhat do you want to update? \n1. Add student \n2. Update student's information \n3. Delete student")
            choice = int(input("\nChoose an option (1 - 3): "))

            if choice == 1:
                name = input("Enter student's name: ")
                birth = input("Enter student's birthday: ")
                gender = input("Enter student's gender: ")

                student.add_student(name, birth, gender)
            
            elif choice == 2:
                student_id = input("\nInsert the student's ID that you would like to update information on: ")
                name = input("Enter student's name: ")
                birth = input("Enter student's birthday: ")
                gender = input("Enter student's gender: ")

                student.update_student(student_id, name, birth, gender)

            else:
                student_id = input("\nInsert the student's ID that you would like to delete: ")

                student.delete_student(student_id)

        elif option == 3:
            student.show_full_list()

        else:
            break

main()