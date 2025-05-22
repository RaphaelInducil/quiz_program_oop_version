# raphael clouiee inducil
# BSCpE 1-2 
# 04-07-25
# assignment 11: Convert assignment 9 and 10 to OOP
# Turn assignment 9 (quiz_maker) and 10 (quiz_program) into OOP

# create class quiz_maker.py oop vers.

class QuizMaker:
    def __init__(self, maker):
        self.maker = maker

    def make(self):
        file_name = input("Enter the name of your quiz (without .txt): ") + ".txt"
        with open(file_name, "w") as file:

            while True:
                    question = input("Enter your question: ")
                    answer_a = input("Enter answer A: ")
                    answer_b = input("Enter answer B: ")
                    answer_c = input("Enter answer C: ")
                    answer_d = input("Enter answer D: ")
                    correct_answer = input("Enter the correct answer: ")

                    file.write("Question: " + question + "\n")
                    file.write("A: " + answer_a + "\n")
                    file.write("B: " + answer_b + "\n")
                    file.write("C: " + answer_c + "\n")
                    file.write("D: " + answer_d + "\n")
                    file.write("Correct Answer: " + correct_answer + "\n")
                    file.write("\n")

                    done = input("do you want to input another question? (yes/no): ")
                    if done.lower() == "no":
                        break
                    elif done.lower() == "yes":
                        continue
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")
                        break

# create class quiz_program.py oop vers.

import random
class QuizProgram:
    quiz_file = input("Enter the name of your quiz file (without .txt): ") + ".txt"

    with open(quiz_file, "r") as file:
        file_lines = file.readlines()

    quiz_data = []
    line_number = 0

    while line_number < len(file_lines):
        if file_lines[line_number].startswith("Question: "):
            question = file_lines[line_number].strip()
            answer_a = file_lines[line_number + 1].strip()
            answer_b = file_lines[line_number + 2].strip()
            answer_c = file_lines[line_number + 3].strip()
            answer_d = file_lines[line_number + 4].strip()
            correct_answer = file_lines[line_number + 5].strip()

            quiz_data.append([
                question,
                answer_a,
                answer_b,
                answer_c,
                answer_d,
                correct_answer
            ])
            line_number += 7

    random.shuffle(quiz_data)

    score = 0

    for quiz_item in quiz_data:
        print("\n" + quiz_item[0])
        print(quiz_item[1])
        print(quiz_item[2])
        print(quiz_item[3])
        print(quiz_item[4])

        user_answer = input("Your answer (A, B, C, D): ").strip().upper()

        correct_answer = quiz_item[5].split(": ")[1].strip().upper()

        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer is: " + correct_answer)

        continue_quiz = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_quiz != "yes":
            print("Thank you for playing!")
            break

    print(f"\nYou got {score} correct out of {len(quiz_data)}.")

# import both projects
# create menu to run the quiz maker and quiz program
    # while loop
    # display menu
    # get user input
    # elif condition for choices
# end