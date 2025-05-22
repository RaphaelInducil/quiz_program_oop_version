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
# import both projects
# create menu to run the quiz maker and quiz program
    # while loop
    # display menu
    # get user input
    # elif condition for choices
# end