phone_book = open("phone_book.txt", "a")

phone_book.write("\nHuy - 12312312xx")
phone_book.write("\nLong - 12332112xx")

phone_book.close()

phone_book = open("new_phone_book.txt", "w")

phone_book.write("\nHuy - 12312312xx")
phone_book.write("\nLong - 12332112xx")

phone_book.close()

phone_book = open("index.html", "w")
phone_book.write("<p>Hello, word!</p>")
phone_book.close()