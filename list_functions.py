student_names = ["Nguyen", "Nguyen", "Hung", "Tuyen", "Trung", "Sang", "Truong"]
math_scores = [10, 9, 8, 7, 6, 5]

print(student_names)

student_names.append("Thang")
print(student_names)

student_names.insert(1, "Dung")
print(student_names)

student_names.remove("Sang")
print(student_names)

student_names.pop()
print(student_names)

print(student_names.index("Tuyen"))

print(student_names.count("Nguyen"))
print(student_names.count("Hung"))

student_names.sort()
print(student_names)

math_scores.sort()
print(math_scores)

math_scores.reverse()
print(math_scores)

student_names_2 = student_names.copy()
print(student_names_2)

student_names.extend(math_scores)
print(student_names)

student_names.clear()
print(student_names)