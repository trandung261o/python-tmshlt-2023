number = 2
text = " la so nguoi yeu ma toi tung co."

print(str(number) + text)

print(f"{number}{text}")

text = "{} la so nguoi yeu ma toi tung co."
print(text.format(number))

my_age = 27
my_wife_age = 25
text = "Nam nay toi {} tuoi. Con vo toi {} tuoi."

print(text.format(my_age, my_wife_age))


text = "Nam nay toi {1} tuoi. Con vo toi {0} tuoi."

print(text.format(my_age, my_wife_age))