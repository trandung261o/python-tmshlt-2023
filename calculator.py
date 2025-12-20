num1 = float(input("Nhap so thu nhat: "))
operator = input("Nhap vao toan tu: ")
num2 = float(input("Nhap so thu hai: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Toan tu khong hop le!!")
