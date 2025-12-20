english_vietnamese_dictionary = {
    "hello": "xin chao",
    "goodbye": "tam biet",
    "morning": "buoi sang",
    "bread": "banh mi",
    "coffee": "ca phe",
    "tea": "tra",
    "milk": "sua",
    "beer": "bia",
    0: "xin chao",
    1: "tam biet",
    2: "buoi sang"
}

print(english_vietnamese_dictionary["tea"])
print(english_vietnamese_dictionary["milk"])
print(english_vietnamese_dictionary.get("beer"))
print(english_vietnamese_dictionary.get("cat", "Tu khoa nay khong ton tai!!!"))
print(english_vietnamese_dictionary[0])
