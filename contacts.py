"""
TASK: Create a ContactBook class.

Requirements:
1. Store contacts in a dictionary (name → phone number).
2. Provide a method to add new contacts.
3. Provide a method to delete contacts.
4. Provide a method to search for a contact by name.
5. Provide a method to show all contacts.

Example Usage:
    book = ContactBook()
    book.add_contact("Alice", "08012345678")
    print(book.search_contact("Alice"))  # "08012345678"
"""

class ContactBook:
    def __init__(self):
        self.contact = {}

    def add_contact(self, name, phone):
        self.contact[name] = {"phone": phone}

    def remove(self, name):
        if name in self.contact[name]:
            del self.contact[name]
            return f"{name} has been deleted"
        else:
            return f"{name} not found contact"

    def search_contact(self, name):
        return self.contact.get(name, f"{name} not found.")
    
    def show_all_contact(self):
        return self.contact
    
book = ContactBook()
book.add_contact("John", "08123456789")
book.add_contact("Mary", "09098765432")

print(book.show_all_contact())
print(book.search_contact("John"))  

book.remove("John")
print(book.show_all_contact())

    