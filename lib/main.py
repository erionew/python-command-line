from connection import Contact



contact_list = Contact.select()

# person = Contact(first_name='person',last_name='one',phone_number='214-212-222')
# person.save()

# person = Contact(first_name='person',last_name='two',phone_number='214-212-223')
# person.save()

def print_contact_book():

    print('Contact Book')
    if len(contact_list) == 0:
        print('Your contacts are empty.')
    else:
        contact_info = [contact.first_name.capitalize() + ' ' + contact.last_name.capitalize() + ' - ' + contact.phone_number for contact in contact_list]
        for contact in contact_info:
            print(f'{contact_info.index(contact)+1}.{contact}')

print_contact_book()


user_input = input('Would you like to add a new contact? (y/n): ')

if user_input == 'y':
    contact_first_name = input('Contact First Name: ')
    contact_last_name = input('Contact Last Name: ')
    contact_phone = input('Contact Phone Number: ')
    print('Contact Added')
else:
    print(':/')