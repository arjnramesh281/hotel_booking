# contacts = {}

# while True:
#     print("Contact Management System")
#     print("1. Add Contact")
#     print("2. View Contacts")
#     print("3. Update Contact")
#     print("4. Delete Contact")
#     print("5. Exit")
#     choice = input("Enter your choice: ")

#     if choice == '1':
#         contact_id = input("Enter Contact ID: ")
#         if contact_id in contacts:
#             print("Contact ID already exists. Please enter a unique ID.\n")
#         else:
#             name = input("Enter Name: ")
#             phone = input("Enter Phone Number: ")
#             email = input("Enter Email: ")
#             contacts[contact_id] = {"name": name, "phone": phone, "email": email}
#             print("Contact added successfully!\n")
    
#     elif choice == '2':
#         if not contacts:
#             print("\nNo contacts available.\n")
#         else:
#             print("\n{:<10} {:<20} {:<15} {:<25}".format("ID", "Name", "Phone", "Email"))
#             print("-" * 70)
#             for contact_id, details in contacts.items():
#                 print("{:<10} {:<20} {:<15} {:<25}".format(contact_id, details['name'], details['phone'], details['email']))
#             print("")

#     elif choice == '3':
#         contact_id = input("Enter Contact ID to update: ")
#         if contact_id in contacts:
#             print("Current Name: " + contacts[contact_id]['name'])
#             new_name = input("Enter new name (leave blank to keep current): ")
#             contacts[contact_id]['name'] = new_name or contacts[contact_id]['name']
            
#             print("Current Phone: " + contacts[contact_id]['phone'])
#             new_phone = input("Enter new phone (leave blank to keep current): ")
#             contacts[contact_id]['phone'] = new_phone or contacts[contact_id]['phone']
            
#             print("Current Email: " + contacts[contact_id]['email'])
#             new_email = input("Enter new email (leave blank to keep current): ")
#             contacts[contact_id]['email'] = new_email or contacts[contact_id]['email']
            
#             print("Contact updated successfully!\n")
#         else:
#             print("Contact not found!\n")
    
#     elif choice == '4':
#         contact_id = input("Enter Contact ID to delete: ")
#         if contact_id in contacts:
#             del contacts[contact_id]
#             print("Contact deleted successfully!\n")
#         else:
#             print("Contact not found!\n")
    
#     elif choice == '5':
#         print("Exiting ")
#         break
    
#     else:
#         print("Invalid choice! Please try again.\n")
