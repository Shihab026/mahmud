# Student Management System
# Author: MD. Shihab Mahmud (you can change this)
# Language: Python

students = []

def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    dept = input("Enter Department: ")
    cgpa = input("Enter CGPA: ")

    student = {
        "ID": sid,
        "Name": name,
        "Department": dept,
        "CGPA": cgpa
    }

    students.append(student)
    print("✅ Student added successfully!\n")


def view_students():
    if not students:
        print("❌ No student records found.\n")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['ID']}, Name: {s['Name']}, Dept: {s['Department']}, CGPA: {s['CGPA']}")
    print()


def search_student():
    sid = input("Enter Student ID to search: ")
    for s in students:
        if s["ID"] == sid:
            print("🎯 Student Found:")
            print(s)
            print()
            return
    print("❌ Student not found.\n")


def update_student():
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s["ID"] == sid:
            s["Name"] = input("Enter new Name: ")
            s["Department"] = input("Enter new Department: ")
            s["CGPA"] = input("Enter new CGPA: ")
            print("✅ Student updated successfully!\n")
            return
    print("❌ Student not found.\n")


def delete_student():
    sid = input("Enter Student ID to delete: ")
    for s in students:
        if s["ID"] == sid:
            students.remove(s)
            print("🗑️ Student deleted successfully!\n")
            return
    print("❌ Student not found.\n")


def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting program. Thank you!")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")


# Program Start
menu()
