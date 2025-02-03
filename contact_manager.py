class Contact:
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}"

def add_contact(contacts, name, email, phone, address):
    if any(contact.phone == phone for contact in contacts):
        print("Error: This phone number already exists!")
        return
    new_contact = Contact(name, email, phone, address)
    contacts.append(new_contact)

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. {contact}")

def remove_contact(contacts, phone):
    for contact in contacts:
        if contact.phone == phone:
            contacts.remove(contact)
            print(f"Contact with phone {phone} removed.")
            return
    print(f"No contact found with phone {phone}.")

def search_contact(contacts, query):
    found_contacts = [contact for contact in contacts if query.lower() in contact.name.lower() or query.lower() in contact.email.lower()]
    if found_contacts:
        for contact in found_contacts:
            print(contact)
    else:
        print("No matching contacts found.")