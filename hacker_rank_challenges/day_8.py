# number_of_contacts = int(input())
#
#
# def address_phone():
#     for n in range(number_of_contacts):
#         name, number = input().split()
#         phonebook_dict[name] = number
#
#
# def find_contact():
#     contact_name = []
#     for n in range(number_of_contacts):
#         query = input()
#         if query in phonebook_dict:
#             print(query + "=" + phonebook_dict[query])
#         else:
#             print("Not found.")
#
#
# phonebook_dict = {}
# address_phone()
# find_contact()
# print(address_phone())

number_of_contacts = int(input("Number of contacts to add: "))
name_numbers = [input("Please enter Name and Number: ").split() for _ in range(number_of_contacts)] # List comprehension
phone_book = {key: value for key, value in name_numbers} # Dictionary comprehension
for _ in range(number_of_contacts):
    name = input("Type name to access contact: ")
    if name in phone_book:
        print('%s=%s' % (name, phone_book[name]))
    else:
        print('Not found')


