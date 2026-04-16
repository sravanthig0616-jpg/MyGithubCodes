import json
import os

FILE = "students.json"

# Load data
def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Add student
def add_student(data):
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    data.append(student)
    save_data(data)
    print("Student added!")

# View students
def view_students(data):
    if not data:
        print("No students found.")
        return
    for s in data:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")

# Search student
def search_student(data):
    roll = input("Enter roll to search: ")
    for s in data:
        if s["roll"] == roll:
            print("Found:", s)
            return
    print("Student not found.")

# Delete student
def delete_student(data):
    roll = input("Enter roll to delete: ")
    new_data = [s for s in data if s["roll"] != roll]
    save_data(new_data)
    print("Deleted if existed.")

# Menu
def main():
    data = load_data()

    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            delete_student(data)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()