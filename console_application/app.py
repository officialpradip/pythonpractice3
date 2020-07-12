
import csv
#global variables
student_fields = ['RollNo', 'Name', 'Course', 'Fee', 'Payment','Remaining']
student_database = 'console_application/test.csv'


def display_menu():
    print("--------------------------------------")
    print(" Welcome to IT Academy Console APP")
    print("---------------------------------------")
    print("1. Register")
    print("2. Course Details")
    print("3. Search Course")
    print("4. Update Details")
    print("5. Delete Details")
    print("6. Quit")


def register():
    print("-------------------------")
    print("Add  Information")
    print("-------------------------")
    global student_fields
    global student_database

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Student is registered sucessfully")
    input("Press Enter to continue")
    return


def view_course():
    global student_fields
    global student_database

    print("--- Course Details ---")
    
    with open("console_application/test.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            print('Course list are:',lines[2])
    input("Press Enter to continue")


def search_course():
    global student_fields
    global student_database

    print("--- Search course by student roll no ---")
    roll = input("Enter roll no. to search: ")
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    print("----- Student Found -----")
                    print("Roll: ", row[0])
                    print("Name: ", row[1])
                    print("Course: ", row[2])
                    print("Remaining Fee: ", row[5])
                    
                    break
        else:
            print("Roll No. not found")
    input("Press Enter to continue")


def update_details():
    global student_fields
    global student_database

    print("--- Update Details ---")
    roll = input("Enter roll no. to update: ")
    index_student = None
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_student = counter
                    print("Student Found: at index ",index_student)
                    student_data = []
                    for field in student_fields:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1

    if index_student is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found")

    input("Press Enter to continue")


def delete_details():
    global student_fields
    global student_database

    print("--- Delete Details ---")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found")

    input("Press Enter to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        register()
    elif choice == '2':
        view_course()
    elif choice == '3':
        search_course()
    elif choice == '4':
        update_details()
    elif choice == '5':
        delete_details()
    else:
        break
print('-----Report using IT Academy console app----------')