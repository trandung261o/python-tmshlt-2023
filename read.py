phone_book = open("phone_book.txt", "r")

print(phone_book.readable())

# print(phone_book.read())

# print(phone_book.readline())
# print(phone_book.readline())
# print(phone_book.readline())

# print(phone_book.readlines())

for person in phone_book.readlines():
    person = person.replace("\n", "")
    print(person)

phone_book.close()