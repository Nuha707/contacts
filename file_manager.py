import os
import csv
from contact_manager import Contact

def save_contacts(contacts, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for contact in contacts:
            writer.writerow([contact.name, contact.email, contact.phone, contact.address])

def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'a') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 4:
                    name, email, phone, address = row
                    contacts.append(Contact(name, email, phone, address))
                else:
                    print(f"Skipping invalid row: {row}")
    return contacts