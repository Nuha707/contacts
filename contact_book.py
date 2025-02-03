from contact_manager import add_contact, view_contacts, remove_contact, search_contact
from file_manager import save_contacts, load_contacts

CONTACTS_FILE = "contacts.txt"
contacts = load_contacts(CONTACTS_FILE)

def display_menu():
    print("Contact Book Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone number: ")
            address = input("Enter address: ")
            print("Contacts added successfully")
            
            try:
                phone = int(phone)  # Ensure phone number is an integer
            except ValueError:
                print("Invalid phone number. Please enter a valid integer.")
                continue

            add_contact(contacts, name, email, phone, address)
            save_contacts(contacts, CONTACTS_FILE)
            
        elif choice == '2':
            view_contacts(contacts)
        
        elif choice == '3':
            phone = input("Enter the phone number of the contact to remove: ")
            try:
                phone = int(phone)
            except ValueError:
                print("Invalid phone number. Please enter a valid integer.")
                continue
            remove_contact(contacts, phone)
            save_contacts(contacts, CONTACTS_FILE)
        
        elif choice == '4':
            query = input("Enter name or email to search: ")
            search_contact(contacts, query)
        
        elif choice == '5':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()