#QUIZ APP
questions = (
"1.How many elements are in the periodic table?: ",

                       "2.who is the India's first prime minister?: ",

                       "3. when did India become independent?: ",
                     " 4.How many bones are in the human body?: ",
                       "5. what is the value of X in the equation 2X + 6 = 16 : ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Jawahar Lal Nehru", "B. Lal Bahadur Shastri", "C. Dr. Rajendra prasad", "D. Indira Gandhi"),
                   ("A. 1950", "B. 1948", "C. 1955", "D. 1947"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. 2", "B. 10", "C. 3", "D. 4"))

answers = ("C", "A", "D", "A", "B")
guesses = []
score = 0
question_num = 0
for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
print("Never give up,keep moving forward ")
print("Thank You")
