def translate(text):
    translation = ""
    for character in text:
        if character.lower() in "áàảãạăắẳẵặâấầẩậ":
            if character.isupper():
                translation += "A"
            else:
                translation += "a"
        else:
            translation += character
    return translation

text = input("Nhap vao van ban ma ban muon dich: ")
print(translate(text))