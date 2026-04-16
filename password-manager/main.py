import json
import os

FILE = "passwords.json"

def load_data():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_password(data):
    site = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    data[site] = {"username": username, "password": password}
    save_data(data)
    print("Saved!")

def view_passwords(data):
    if not data:
        print("No data found")
        return
    for site, info in data.items():
        print(f"{site} -> {info['username']} / {info['password']}")

def search_password(data):
    site = input("Enter website: ")
    if site in data:
        print(data[site])
    else:
        print("Not found")

def delete_password(data):
    site = input("Enter website to delete: ")
    if site in data:
        del data[site]
        save_data(data)
        print("Deleted")
    else:
        print("Not found")

def main():
    data = load_data()

    while True:
        print("\n1. Add Password")
        print("2. View All")
        print("3. Search")
        print("4. Delete")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_password(data)
        elif choice == "2":
            view_passwords(data)
        elif choice == "3":
            search_password(data)
        elif choice == "4":
            delete_password(data)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()