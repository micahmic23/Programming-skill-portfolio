"""Maths Quiz, Ex.1"""

# Imports the all modules and functions of the tkinter GUI toolkit from Python's Library.
from tkinter import *

# Imports random generated numbers taken from the Library.
import random

# The class 'MathsQuiz' sets the main window and frames created to be used later on.
maths = Tk() # Initializes the GUI toolkit.
maths.title("Maths Quiz, Ex.1") # Creates a title.
maths.resizable(width = False, height = False) # fixed window size.
maths.geometry('600x300') # Sets the window's width and height.
maths.configure(bg = "#fadad9") # Sets background color.

scorez = 0
num_questions = 0
lvl = 1
no1 = 0
no2 = 0
operation = ''
correctAns = 0
firstAttempt = True
        
menuFrame = Frame(maths, bg = "#fadad9")
quizFrame = Frame(maths, bg = "#fadad9")


    
# The function creates the Menu section of the quiz. This consists of a label class and three buttons to select the desired level.
def displayMenu():
    menuFrame.pack() # Displays the class elements within the menuFrame created.
    Label(menuFrame, text = "Please Select a Difficulty Level ૮ ˶ᵔ ᵕ ᵔ˶ ა", font = ("Arial", 28), bg = "#fadad9").pack(pady = 30)
    Button(menuFrame, text = "Easy", command = lambda: set_level(1), font = ("Arial", 20), bg = "white").pack(pady = 5)
    Button(menuFrame, text = "Moderate", command = lambda: set_level(2), font = ("Arial", 20), bg = "white").pack(pady = 5)
    Button(menuFrame, text = "Advanced", command = lambda: set_level(3), font = ("Arial", 20), bg = "white").pack(pady = 5)
        
# Sets the difficulty level chosen from the menu section and once again sets the scoring and questions to be displayed.
def set_level(level):
    global lvl, scorez, num_questions
    lvl = level
    scorez = 0
    num_questions = 0
    menuFrame.pack_forget()
    quizFrame.pack()
    displayProblem()
    
# Produces random numbers based on the difficulty chosen.
def randomInt():
    if lvl == 1:
        return random.randint(1, 9), random.randint(1, 9) # Generates single digit numbers.
    elif lvl == 2:
        return random.randint(10, 99), random.randint(10, 99) # Generates double digit numbers.
    elif lvl == 3:
        return random.randint(1000, 9999), random.randint(1000, 9999) # Generates four digit numbers.
    
# Randomly displays either addition or subtraction for the questions.
def decideOperation():
    return random.choice(['+','-'])
    
# A function that displays a new problem when the sum of questions generated are below 10. If not, it calls the function 'displayResults' for the score and grading.
def displayProblem():
    global no1, no2, operation, correctAns, firstAttempt
    if num_questions >= 10:
            displayResults()
            return
    no1, no2 = randomInt() # Generates random numbers for the questions.
    operation = decideOperation() # Generates either addition or subtration for the questions.
    correctAns = no1 + no2 if operation == '+' else no1 - no2
    firstAttempt = True
            
    # Empties the quizFrame to display the new question.
    for widget in quizFrame.winfo_children():
        widget.destroy()
            
    # Displays a new random question through a Label class. 
    Label(quizFrame, text = f"{no1} {operation} {no2} =", font = ("Arial", 20), bg = "#fadad9").pack(pady = 40)
        
    # An entry class to type your answer.
    global ansEntry
    ansEntry = Entry(quizFrame)
    ansEntry.pack(pady = 5)
        
    # A button to submit your answer. Commands the function 'isCorrect' for checking whether the answer is correct or incorrect.
    Button(quizFrame, text = "Submit your Answer", command = isCorrect, font = ("Arial", 20), bg = "#fadad9").pack(pady = 5)
        
# Verifies the answer and grades the user on its first and second attempt. Provides a message whether the answer is correct or not.
def isCorrect():
    global scorez, num_questions, firstAttempt
    try:
        ans = int(ansEntry.get()) # Inputs the typed answer as ans.
        if ans == correctAns: # Condition to check if the answer matches the right answer.
            scorez += 10 if firstAttempt else 5 # Give 10 points for first attempt otherwise 5 is given.
            Label(quizFrame, text = "Correct! ໒꒰ྀིᵔ ᵕ ᵔ ꒱ྀི১",  fg = "green", font = ("Arial", 18), bg = "#fadad9").pack() # Displays a message to say that the answer is correct.
            num_questions += 1 # Implements the number of questions by 1 to count the number of questions that are generated or answered.
            maths.after(1500, displayProblem) # Pauses the current question for 1.5 milliseconds then calls the displayProblem function to generate a new one.
        else: # Otherwise (When the first attempt is wrong).
            if firstAttempt:
                firstAttempt = False
                Label(quizFrame, text = "Incorrect! ૮꒰ྀི⸝⸝> . <⸝⸝꒱ྀིა.", fg = "red", font = ("Arial", 18), bg = "#fadad9").pack() # A message is displayed conveying that the answer is incorrect, which proceeds to letting you answer again.
                num_questions += 1 # Implements the number of questions by 1 to count the number of questions that are generated or answered.
                maths.after(1500, displayProblem) # Pauses the current question for 1.5 milliseconds then calls the displayProblem function to generate a new one.
    except ValueError: # When the value is not an integer. A message is sent to enter a valid number.
        Label(quizFrame, text = "Please enter a valid number. (๑﹏๑//)", fg = "#EF6F68", font = ("Arial", 18), bg = "#fadad9").pack()
            
# Displays the result section of the quiz.  
def displayResults():
    quizFrame.pack_forget() # Clears the quizFrame.
    resultFrame = Frame(maths, bg = "#fadad9") # Displays the frame for the result elements and the buttons below.
    resultFrame.pack(pady=30)
        
    # Displays the final score using a label class.
    Label(resultFrame, text = f"Your Final Score: {scorez}/100", font = ("Arial", 30), bg = "#fadad9").pack(pady = 10)
    # The variable grade stores a conditional statement to check the grade based on the score given.
    grade = "A+" if scorez >= 90 else "A ( ദ്ദി ˙ᗜ˙ )" if scorez >= 80 else "B (ㅅ´ ˘ `)" if scorez >= 70 else "C (๑ᵔ⤙ᵔ๑)" if score >= 60 else "F ૮(˶╥︿╥)ა"
    # Displays the grade.
    Label(resultFrame, text = f"Your grade is: {grade}", font = ("Arial", 30), bg = "#fadad9").pack(pady = 5)
        
    # A play again button to repeat the maths quiz game leading the user back to the menu by calling the displayMenu function.
    Button(resultFrame, text = "Play Again! ৻(  •̀ ᗜ •́  ৻)", command = lambda: [resultFrame.pack_forget(), displayMenu()], font = ("Arial", 20), bg = "#fadad9").pack(pady = 20)
    # A quit button to let the user end the game.
    Button(resultFrame, text = "Exit ૮₍ ˶ᵔ ᵕ ᵔ˶ ₎ა", command = maths.quit, font = ("Arial", 20), bg = "#fadad9").pack(pady = 5)

# Operates the whole maths quiz program.
displayMenu()
maths.mainloop()
