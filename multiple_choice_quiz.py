from Quiz import Quiz

questions = [
    "Cau 1. Doi bong nao ve nhi WC nam 1994?\nA. Brazil \nB. Italia \nC. Duc\n",
    "Cau 2. Doi bong nao vo dich WC nam 1998? \nA. Argentina \nB. Phap \nC. Brazil\n",
    "Cau 3. Nuoc nao la chu nha WC nam 2002? \nA. Qatar \nB. Duc \nC. Han Quoc + Nhat Ban\n"
]

quizzes = [
    Quiz(questions[0], "B"),
    Quiz(questions[1], "B"),
    Quiz(questions[2], "C")
]

def run_quizzes(quizzes):
    score = 0
    for quiz in quizzes:
        print(quiz.question)
        user_input = input("Nhap cau tra loi cua ban: ")
        if user_input.lower() == quiz.answer.lower():
            score += 1
    print(f"\n--> KET QUA: ban da tra loi dung {score}/{len(quizzes)} cau!")

run_quizzes(quizzes)