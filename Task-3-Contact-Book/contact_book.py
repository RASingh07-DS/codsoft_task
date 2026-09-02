contacts = []

def add_contact():
    print("\n===== ADD CONTACT =====")

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("\nNo contacts found.")
        return

    print("\n===== CONTACT LIST =====")

    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    if not contacts:
        print("\nNo contacts available.")
        return

    keyword = input("\nEnter name or phone number to search: ").strip().lower()
    found = False

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print("\nName:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    view_contacts()

    if not contacts:
        return

    try:
        number = int(input("\nEnter contact number to update: "))

        if 1 <= number <= len(contacts):
            contact = contacts[number - 1]

            name = input(f"Enter new name ({contact['name']}): ").strip()
            phone = input(f"Enter new phone ({contact['phone']}): ").strip()
            email = input(f"Enter new email ({contact['email']}): ").strip()
            address = input(f"Enter new address ({contact['address']}): ").strip()

            if name:
                contact["name"] = name
            if phone:
                contact["phone"] = phone
            if email:
                contact["email"] = email
            if address:
                contact["address"] = address

            print("Contact updated successfully.")
        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")

def delete_contact():
    view_contacts()

    if not contacts:
        return

    try:
        number = int(input("\nEnter contact number to delete: "))

        if 1 <= number <= len(contacts):
            contacts.pop(number - 1)
            print("Contact deleted successfully.")
        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you for using Contact Book.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
