contacts = []

def show_menu():
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        i = 1
        for contact in contacts:
            print("\nContact", i)
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            i = i + 1

def search_contact():
    name_to_search = input("Enter name to search: ")
    found = False

    for contact in contacts:
        if contact["name"].lower() == name_to_search.lower():
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            found = True

    if found == False:
        print("Contact not found.")

def delete_contact():
    view_contacts()

    if len(contacts) == 0:
        return

    number = int(input("Enter contact number to delete: "))

    if number > 0 and number <= len(contacts):
        contacts.pop(number - 1)
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice.")