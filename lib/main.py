from connection import Contact

print('Contact Book')

person = Contact(first_name='person',last_name='one',phone_number='214-212-222')
person.save()

contact_list = Contact.select()

print([contact.first_name for contact in contact_list])