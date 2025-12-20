secret_word = "Python"
hint = "Goi y: Day la ten mot ngon ngu lap trinh"
guess = ""
guess_count = 0
guess_limit = 3

print(hint)

while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("Ban doan day la tu gi? ")
        guess_count += 1
    else:
        break

if guess == secret_word:
    print("BAN DA DOAN CHINH XAC!")
else:
    print("BAN DA THAT BAI VI DOAN SAI 3 LAN!")