print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    print("Okay, maybe next time!")
    quit()
print("Okay! Let's play :)")
score = 0

# Define questions and answers as a list of tuples
questions_answers = [
    ("What does CPU stand for? ", "central processing unit"),
    ("What does GPU stand for? ", "graphics processing unit"),
    ("What does RAM stand for? ", "random access memory"),
    ("What does PSU stand for? ", "power supply"),
    ("What does HDD stand for? ", "hard disk drive"),
    ("What does SSD stand for? ", "solid state drive")
]

for question, correct_answer in questions_answers:
    answer = input(question)
    if answer.lower() == correct_answer:
        print('Correct!')
        score += 1
    else:
        print("Incorrect! The correct answer is:", correct_answer)

print("You got", score, "out of", len(questions_answers), "questions correct!")
percentage = (score / len(questions_answers)) * 100
print("You got {:.2f}%.".format(percentage))
