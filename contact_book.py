# ====================================================
# SBA 351 - Python Essentials 1: Contact Book Application
# Filename: contact_book.py
# ====================================================

def display_menu():
    """Displays the main menu options to the user."""
    print("\n==============================")
    print("      📞 CONTACT BOOK         ")
    print("==============================")
    print("1. View All Contacts")
    print("2. Add a New Contact")
    print("3. Search for a Contact")
    print("4. Delete a Contact")
    print("5. Exit")
    print("==============================")

def view_contacts(contacts):
    """Displays all stored contacts in the dictionary."""
    if not contacts:
        print("\n📭 Your contact book is currently empty.")
        return
    
    print("\n--- SAVED CONTACTS ---")
    # Loop through the dictionary items (name as key, info dict as value)
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"  Phone: {info.get('phone', 'N/A')}")
        print(f"  Email: {info.get('email', 'N/A')}")
        print("-" * 22)

def add_contact(contacts):
    """Prompts the user for contact details and adds them to the dictionary."""
    name = input("\nEnter contact's full name: ").strip().title()
    
    if not name:
        print("❌ Error: Name cannot be blank.")
        return
        
    if name in contacts:
        print(f"⚠️ Warning: {name} already exists in your contacts.")
        update = input("Do you want to update their info? (y/n): ").lower()
        if update != 'y':
            return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address (optional): ").strip()
    
    # Store contact details inside a nested dictionary using the name as the primary key
    contacts[name] = {
        "phone": phone,
        "email": email if email else "N/A"
    }
    print(f"✅ Success! {name} has been added to your contacts.")

def search_contact(contacts):
    """Searches for a specific contact by name."""
    name = input("\nEnter the name of the contact to search: ").strip().title()
    
    # Efficient O(1) dictionary key lookup
    if name in contacts:
        info = contacts[name]
        print(f"\n🔍 Found Contact: {name}")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")
    else:
        print(f"❌ Error: '{name}' was not found in your contact book.")

def delete_contact(contacts):
    """Deletes a contact from the dictionary by name."""
    name = input("\nEnter the name of the contact to delete: ").strip().title()
    
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Success! {name} has been removed from your contacts.")
    else:
        print(f"❌ Error: '{name}' does not exist in your contacts.")

def main():
    """Main execution loop for the Contact Book application."""
    # Dictionary to store contacts { "Name": {"phone": "...", "email": "..."} }
    contact_book = {}
    
    print("Welcome to your interactive Contact Book!")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("❌ Invalid input! Please enter a numerical digit between 1 and 5.")
            continue
            
        if choice == 1:
            view_contacts(contact_book)
        elif choice == 2:
            add_contact(contact_book)
        elif choice == 3:
            search_contact(contact_book)
        elif choice == 4:
            delete_contact(contact_book)
        elif choice == 5:
            print("\nThank you for using Contact Book. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please choose a number from 1 to 5.")

# Entry point safeguard
if __name__ == "__main__":
    main()