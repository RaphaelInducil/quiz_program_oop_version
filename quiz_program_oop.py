# raphael clouiee inducil
# BSCpE 1-2 
# 05-22-25
# assignment 11: Convert assignment 9 and 10 to OOP
# Turn assignment 9 (quiz_maker) and 10 (quiz_program) into OOP

# create class quiz_program.py oop vers.

import random

class QuizProgram:
    def __init__(self):
        self.quiz_data = []

    def load_quiz(self):
        quiz_file = input("Enter the name of your quiz file (without .txt): ") + ".txt"
        try:
            with open(quiz_file, "r") as file:
                file_lines = file.readlines()

            self.quiz_data = []
            line_number = 0

            while line_number < len(file_lines):
                if file_lines[line_number].startswith("Question: "):
                    question = file_lines[line_number].strip()
                    answer_a = file_lines[line_number + 1].strip()
                    answer_b = file_lines[line_number + 2].strip()
                    answer_c = file_lines[line_number + 3].strip()
                    answer_d = file_lines[line_number + 4].strip()
                    correct_answer = file_lines[line_number + 5].strip()

                    self.quiz_data.append([
                        question,
                        answer_a,
                        answer_b,
                        answer_c,
                        answer_d,
                        correct_answer
                    ])
                    line_number += 7

            random.shuffle(self.quiz_data)

        except FileNotFoundError:
            print("File nto found.")

    def take_quiz(self):
        if not self.quiz_data:
            print("No quiz data loaded. Please load a quiz file first.")
            return
            
        score = 0

        for quiz_item in self.quiz_data:
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

        print(f"\nYou got {score} correct out of {len(self.quiz_data)}.")

# done