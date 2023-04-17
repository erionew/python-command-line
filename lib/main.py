from connection import Contact

def handle_user_input():
    user_input = input('Type ADD NEW to add a new contact. In order to find a contact, type their first name. Type DONE when finished: ')
    if user_input == 'DONE':
        print('Exiting...')
    elif user_input == 'ADD NEW':
        contact_first_name = input('Contact First Name: ')
        contact_last_name = input('Contact Last Name: ')
        contact_phone = input('Contact Phone Number: ')
        new_contact = Contact(first_name=contact_first_name, last_name=contact_last_name, phone_number=contact_phone)
        new_contact.save()
        print('Contact Added')
        print_contact_book()
    else:
        print('Finding contact...')
        finding_contact = Contact.get(Contact.first_name == user_input)
        print(finding_contact.first_name.capitalize() + ' ' + finding_contact.last_name.capitalize() + ' - ' + finding_contact.phone_number)

def print_contact_book():
    contact_list = Contact.select()
    print('Contact Book')
    if len(contact_list) == 0:
        print('Your contacts are empty.')
    else:
        contact_info = [contact.first_name.capitalize() + ' ' + contact.last_name.capitalize() + ' - ' + contact.phone_number for contact in contact_list]
        for contact in contact_info:
            print(f'{contact_info.index(contact)+1}.{contact}')
    handle_user_input()
    
    

print_contact_book()
 

