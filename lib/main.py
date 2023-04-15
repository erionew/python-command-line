from connection import Contact

print('Contact Book')


contact_list = Contact.select()

person = Contact(first_name='person',last_name='one',phone_number='214-212-222')
person.save()

person = Contact(first_name='person',last_name='two',phone_number='214-212-223')
person.save()

if len(contact_list) == 0:
     print('Your contacts are empty.')
else:
     contact_info = [contact.first_name.capitalize() + ' ' + contact.last_name.capitalize() + ' - ' + contact.phone_number for contact in contact_list]
     for contact in contact_info:
        print(f'{contact_info.index(contact)+1}.{contact}')

