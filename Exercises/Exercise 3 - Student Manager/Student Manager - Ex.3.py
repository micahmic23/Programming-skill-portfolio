#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 3 - Student Manager 

Created on Wed Oct 30 14:12:51 2024

@author: geronimojo
"""
# Imports the all modules and functions of the tkinter GUI toolkit from Python's Library.
import tkinter as tk
# Imports the ttk module to access Tk themed widgets.
from tkinter import ttk
# Imports the os module for file handling.
import os

# Sets the main window for the student record.
stud = tk.Tk() # Initializes the GUI toolkit.
stud.title("Student Manager, Ex.3") # Creates a title.
stud.geometry("600x500") # Sets the window's width and height.
stud.configure(bg = "#f4e6cb") # Sets background color.
stud.resizable(width = False, height = False) # fixed window size.

# The function that loads the student record from the file
def loadStud_data(filePath):
    if not os.path.isfile(filePath): # Verifies file existence.
        return [] # Retrieves an empty list.
    with open(filePath, 'r') as file: # Accesses file in read mode.
        Data_ = file.readlines() # Scans through all the lines of data.
    studentZ = [] # Empties the student list.
    for line in Data_[1:]: # Starts at the second line.
        section = line.strip().split(',') # Divides each line with commas ",".
        stud_num = section[0] # Accesses the student number.
        _name = section[1] # Accesses the student name.
        _coursework = list(map(int,section[2:5])) # Changes the coursework marks to integers.
        _exam = int(section[5]) # Changes the exam mark to an integer.
        _sumCoursework = sum(_coursework) # Calculates the sum of coursework marks.
        _sumMarks = _sumCoursework + _exam # Calculates the sum of all the marks.
        _percentage = (_sumMarks / 160) * 100 # Calculates the student's percentage.
        _grade = calcuGrade(_percentage) # Grades student according to percentage.
        studentZ.append((stud_num, _name, _sumCoursework, _exam, _percentage, _grade)) # Adds the new items to the list.
    return studentZ # Returns the students' list including the new data calculated.

# Decides student grade based on percentage calculated.
def calcuGrade(_percentage):
    if _percentage >= 70:
        return 'A, Exceeds Expectations'
    elif _percentage >= 60 and _percentage <=69:
        return 'B, Meets Expectations'
    elif _percentage >=50 and _percentage <=59:
        return 'C, Near Expectations'
    elif _percentage >=40 and _percentage <=49:
        return 'D, Below Expectations'
    else: 
        return 'F, No Evidence of Learning'
    
# Lists out all student records in the text box area.
def show_studRecords():
    displayText.delete(1.0,tk.END) # Empties out the text box
    for student in studentZ:
        # Displays text that shows each student's data.
        displayText.insert(tk.END, f"Student Name: {student[1]}\n") 
        displayText.insert(tk.END, f"Student Number: {student[0]}\n")
        displayText.insert(tk.END, f"Total Coursework Mark: {student[2]}\n")
        displayText.insert(tk.END, f"Exam Mark: {student[3]}\n")
        displayText.insert(tk.END, f"Overall Percentage: {student[4]:.2f}%\n")
        displayText.insert(tk.END, f"Student Grade: {student[5]}\n\n")
    # Calculates the average percentage of students obtained.
    _avgPercentage = sum(student[4] for student in studentZ) / len(studentZ) if studentZ else 0
    displayText.insert(tk.END, f"Number of Students: {len(studentZ)}\n") # Displays number of students.
    displayText.insert(tk.END, f"Average Percentage: {_avgPercentage:.2f}%\n") # Displays the average percentage achieved.
    
# Showcases the student with the highest score.
def show_highScore():
    _highestStud = max(studentZ, key = lambda s: s[4]) # Searches for the student with the highest percentage.
    _showStud(_highestStud) # Displays the highest student's information.
    
# Showcases the student with the lowest score.
def show_lowScore():
    _lowestStud = min(studentZ, key = lambda s: s[4]) # Searches for the student with the lowest percentage.
    _showStud(_lowestStud) # Displays the lowest student's information.
    
# Exhibits an individual student record.
def _showStud(student):
    displayText.delete(1.0,tk.END) # Empties out the text box area.
    # Displays text that shows each inividual student's data.
    displayText.insert(tk.END, f"Student Name: {student[1]}\n")
    displayText.insert(tk.END, f"Student Number: {student[0]}\n")
    displayText.insert(tk.END, f"Total Coursework Mark: {student[2]}\n")
    displayText.insert(tk.END, f"Exam Mark: {student[3]}\n")
    displayText.insert(tk.END, f"Overall Percentage: {student[4]:.2f}%\n")
    displayText.insert(tk.END, f"Student Grade: {student[5]}\n")
    
# Exhibits the selected student record from the dropdown.
def show_selectStud():
    _selectIndex = studDropwn.current() # Curremt student selected from dropdown.
    if _selectIndex != -1:
        _showStud(studentZ[_selectIndex]) # Displays the selected student's record.
        
# Displays the main heading.
headTitle = tk.Label(stud, text = "Student Record Manager", bg = "#f4e6cb", font = ("Arial", 24, "bold"))
headTitle.pack(pady = 20)

# Imports student information from the file given below.
studentZ = loadStud_data("/Users/geronimojo/Desktop/studentMarks.txt")

# Displays frame for interactive buttons.
bttnFrame = tk.Frame(stud, bg = "#f4e6cb")
bttnFrame.pack(pady = 10)

# Creates button to display all of the student records.
show_recordBttn = tk.Button(bttnFrame, text = "View All Records", bg = "#f4e6cb", font = ("Arial", 15), command = show_studRecords)
show_recordBttn.grid(row = 0, column = 0, padx = 5) # Sets position to left side.

# Creates button to display the highest scoring student.
highest_scoreBttn = tk.Button(bttnFrame, text = "Highest Score", bg = "#f4e6cb", font = ("Arial", 15), command = show_highScore)
highest_scoreBttn.grid(row = 0, column = 1, padx = 5)

# Creates button to display the lowest scoring student.
lowest_scoreBttn = tk.Button(bttnFrame, text = "Lowest Score", bg = "#f4e6cb",font = ("Arial", 15), command = show_lowScore)
lowest_scoreBttn.grid(row = 0, column = 2, padx = 5)

# Displays frame for viewing individual records.
selectFrame = tk.Frame(stud, bg = "#f4e6cb")
selectFrame.pack(pady = 10)

# Creates a text to display individual student's data from the dropdown.
show_select = tk.Label(selectFrame, text = "View Individual Student Record:", bg = "#f4e6cb", font = ("Arial", 12))
show_select.grid(row = 0, column = 0, padx = 5)

# Displays a dropdown menu to choose using the student name.
studDropwn = tk.ttk.Combobox(selectFrame, values = [student[1] for student in studentZ], state = "readonly")
studDropwn.grid(row = 0, column = 1, padx = 5)

#Displays the view record button.
selectBttn = tk.Button(selectFrame, text = "View Record", bg = "#f4e6cb", font = ("Arial", 12), command = show_selectStud)
selectBttn.grid(row = 0, column = 2, padx = 5)

# Creates a text box to showcase student records.
displayText = tk.Text(stud, height = 15, width = 70, font = ("Arial", 12))
displayText.pack(pady = 20)

# Runs the student manager program app.
stud.mainloop()

    
        
    


