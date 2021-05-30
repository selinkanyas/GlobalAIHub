q1 = "In what year was Şef born?"
q2 = "Who is Emir in love with?"
q3 = "In which city was Selin born?"
q4 = "Who is Ferhat's favorite resident?"
q5 = "How many kg of food is Şef capable of eating in a day?"

answer1 = "2019"
answer2 = "Selin"
answer3 = "İzmir"
answer4 = "Selin"
answer5 = "20"

QuestionsList = [q1 , q2 , q3 , q4 , q5 ]
AnswersList = [ answer1 , answer2 , answer3 , answer4 , answer5 ]

score = 0

for i in range(len(QuestionsList)):
    question = input(QuestionsList[i])
    answer = AnswersList[i]

    if question == answer:
        print("Bravo! 10 points.")
        score = score + 10
    else:
        print("Wrong answer.")


print("You got " + str(score) + " out of 50.")
if score > 25:
    print("You pass!")
else:
    print("You fail!")
