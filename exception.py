
try:
    print(text)
except:
    print("Co loi xay ra, vui long lien he trung tam tu van de duoc ho tro.")

try:
    num1 = int(input("Nhap vao tu so: "))
    num2 = int(input("Nhap vao mau so: "))
    result = num1 / num2
    print(f"Thuong cua phep chia la: {result}")
except ZeroDivisionError:
    print("Mau so phai khac 0. Vui long nhap lai!")
except ValueError:
    print("Du lieu dau vao phai la so nguyen. Vui long nhap lai!")
except:
    print("Co loi xay ra, vui long lien he trung tam tu van de duoc ho tro.")