#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 03:50:42 2024

@author: geronimojo
"""

# Imports the all modules and functions of the tkinter GUI toolkit from Python's Library.
import tkinter as tk
# Imports the ttk module to access Tk themed widgets.
from tkinter import ttk
# Imports messagebox to display messages.
from tkinter import messagebox
# Imports the os module for file handling.
import os

# Sets the main window for the student record.
stud = tk.Tk() # Initializes the GUI toolkit.
stud.title("Student Manager, Ex.3 (Bonus)") # Creates a title.
stud.geometry("800x900") # Sets the window's width and height.
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
        displayText.insert(tk.END, _showStud(student)) 
    # Calculates the average percentage of students obtained.
    _avgPercentage = sum(student[4] for student in studentZ) / len(studentZ) if studentZ else 0
    displayText.insert(tk.END, f"Number of Students: {len(studentZ)}\n") # Displays number of students.
    displayText.insert(tk.END, f"Average Percentage: {_avgPercentage:.2f}%\n") # Displays the average percentage achieved.
    
# Exhibits an individual student record.
def studForm(student):
    # Displays text that shows each inividual student's data.
    return (f"Student Name: {student[1]}\n"
            f"Student Number: {student[0]}\n"
            f"Total Coursework Mark: {student[2]}\n"
            f"Exam Mark: {student[3]}\n"
            f"Overall Percentage: {student[4]:.2f}%\n"
            f"Student Grade: {student[5]}\n\n")    
    
# Showcases the student with the highest score.
def show_highScore():
    _highestStud = max(studentZ, key = lambda s: s[4]) # Searches for the student with the highest percentage.
    _showStud(_highestStud) # Displays the highest student's information.
    
# Showcases the student with the lowest score.
def show_lowScore():
    _lowestStud = min(studentZ, key = lambda s: s[4]) # Searches for the student with the lowest percentage.
    _showStud(_lowestStud) # Displays the lowest student's information.
    
# Clears all text to display a new student record from studForm.
def _showStud(student):
    displayText.delete(1.0, tk.END)
    displayText.insert(tk.END, studForm(student))

# Allows a new student record to be added to the manager.
def addStud_rec():
    # Enters and calculates new student data.
    stud_num = stud_num_entry.get() 
    _name = _name_entry.get()
    _coursework1 = int(_coursework1_entry.get())
    _coursework2 = int(_coursework2_entry.get())
    _coursework3 = int(_coursework3_entry.get())
    _exam = int(_exam_entry.get())
    _sumCoursework = _coursework1 + _coursework2 + _coursework3
    _sumMarks = _sumCoursework + _exam
    _percentage = (_sumMarks / 160) * 100
    _grade = calcuGrade(_percentage)
    newStud = (stud_num, _name, _sumCoursework, _exam, _percentage, _grade)
    studentZ.append(newStud) # Adds the new student record as newStud.
    saveFile() # Saves the file.
    stud_dropwnUpdate() # Updates the student dropdown.
    messagebox.showinfo("Dear User","Student Record Added Successfully!") # Sends a message. 
    
# Deletes a student record, removing it from the manager
def delStud_rec():
    selectStud = studDropwn.get() # Selects a student from the dropdrown to delete.
    global studentZ # Accessing the file to modify.
    studentZ = [s for s in studentZ if s[1] != selectStud] # Deletes the selected student record.
    saveFile() # Saves the file.
    stud_dropwnUpdate() # Updates the student dropdown.
    messagebox.showinfo("Dear User","Student Record Deleted Successfully!") # Sends a message.

# Updates the student record when modified or changed.
def updateStud_rec():
    selectStud = studDropwn.get() # Selects an individual student record.
    # Searches the index of the selected student from the list.
    studIndex = next((i for i, s in enumerate(studentZ) if s[1] == selectStud), None)
    if studIndex is not None:
        fieldUpdate = field_vari.get() # Selects a field to update the record.
        if fieldUpdate == "Student Name": 
            # Updates the student's name.
            studentZ[studIndex] = (studentZ[studIndex][0], _name_entry.get(), studentZ[studIndex][2],
                                        studentZ[studIndex][3], studentZ[studIndex][4], studentZ[studIndex][5])
        elif fieldUpdate == "Total Coursework":
            # Updates coursework marks and calculates the sum of the three courseworks.
            _coursework1 = int(_coursework1_entry.get())
            _coursework2 = int(_coursework2_entry.get())
            _coursework3 = int(_coursework3_entry.get())
            _sumCoursework = _coursework1 + _coursework2 + _coursework3
            studentZ[studIndex] = (studentZ[studIndex][0], studentZ[studIndex][1],
                                        _sumCoursework, studentZ[studIndex][3], 
                                        studentZ[studIndex][4], studentZ[studIndex][5])
        elif fieldUpdate == "Exam Mark":
            # Updates the student's exam mark.
            studentZ[studIndex] = (studentZ[studIndex][0], studentZ[studIndex][1],
                                        studentZ[studIndex][2], int(_exam_entry.get()), 
                                        studentZ[studIndex][4], studentZ[studIndex][5])
        saveFile() # Saves newly updated list to the student data file.
        stud_dropwnUpdate() # Updates the student dropdown.
        messagebox.showinfo("Dear User", "Student Record Updated Successfully!") # Sends a message.

# A function that saves all the student records to the file.
def saveFile():
    with open('/Users/geronimojo/Desktop/studentMarks.txt', 'w') as file:
        file.write("Student Number,Student Name,Coursework1,Coursework2,Coursework3,Exam Mark\n")
        # Writes each individual student record to the file.
        for student in studentZ:
            file.write(f"{student[0]},{student[1]},{student[2]},{student[3]}\n")

# Sorts the student records based on their percentage.
def sortStud_rec():
    _order = _order_vari.get() # Selects the sort order.
    if _order == "Ascending":
        sortStud = sorted(studentZ, key=lambda s: s[4]) # Sorts in ascending order.
    else:
        sortStud = sorted(studentZ, key=lambda s: s[4], reverse=True) # Sorts in descending order.
    displayText.delete(1.0, tk.END) # Empties the current text.
    # Displays the sorted student records.
    for student in sortStud:
        displayText.insert(tk.END, studForm(student))

# Updates the student dropdown list with the student names.
def stud_dropwnUpdate():
    studDropwn['values'] = [student[1] for student in studentZ] # Student name List.
    
# Sets the variable to keep the sorting order.
_order_vari = tk.StringVar(value = "Ascending")

# Creates and displays GUI components.
# Creates the Header Label.
headLabel = tk.Label(stud, text="Student Record Manager", font=("Arial", 24, "bold"), bg = "#f4e6cb")
headLabel.pack(pady=10)

# A frame to contain the buttons elements.
menuFrame = tk.Frame(stud, bg = "#f4e6cb")
menuFrame.pack(pady=10)

# Displays the buttons to be contained in the menuFrame.
bttns = [
    ("Display All Records", show_studRecords),
    ("Show Highest Score", show_highScore),
    ("Show Lowest Score", show_lowScore),
    ("Sort Records", sortStud_rec),
    ("Add Student Record", addStud_rec),
    ("Delete Student Record", delStud_rec),
    ("Update Student Record", updateStud_rec),
]

# Displays all the buttons above and sets its position.
for i, (txt, cmmd) in enumerate(bttns):
    bttn = tk.Button(menuFrame, text=txt, command=cmmd, bg="#f7dcaa", font=("Arial", 15), width=19)
    bttn.grid(row=i // 3, column=i % 3, padx=5, pady=5, sticky="ew")

# A frame to contain the form inputs.
formFrame = tk.Frame(stud, bg="#f4e6cb")
formFrame.pack(pady=10)

# Displays the Student Number entry field.
tk.Label(formFrame, text="Student Number", bg = "#f4e6cb").grid(row=0, column=0, padx=5, pady=5, sticky='e')
stud_num_entry = tk.Entry(formFrame)
stud_num_entry.grid(row=0, column=1, padx=5, pady=5)

# Displays the Student Name entry field
tk.Label(formFrame, text="Student Name", bg = "#f4e6cb").grid(row=1, column=0, padx=5, pady=5, sticky='e')
_name_entry = tk.Entry(formFrame)
_name_entry.grid(row=1, column=1, padx=5, pady=5)

# Display Coursework Marks entry field.
tk.Label(formFrame, text="Coursework Mark 1", bg = "#f4e6cb").grid(row=2, column=0, padx=5, pady=5, sticky='e')
_coursework1_entry = tk.Entry(formFrame)
_coursework1_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(formFrame, text="Coursework Mark 2", bg = "#f4e6cb").grid(row=3, column=0, padx=5, pady=5, sticky='e')
_coursework2_entry = tk.Entry(formFrame)
_coursework2_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(formFrame, text="Coursework Mark 3", bg = "#f4e6cb").grid(row=4, column=0, padx=5, pady=5, sticky='e')
_coursework3_entry = tk.Entry(formFrame)
_coursework3_entry.grid(row=4, column=1, padx=5, pady=5)

# Display Exam Mark entry field
tk.Label(formFrame, text="Exam Mark", bg = "#f4e6cb").grid(row=5, column=0, padx=5, pady=5, sticky='e')
_exam_entry = tk.Entry(formFrame)
_exam_entry.grid(row=5, column=1, padx=5, pady=5)

# Dropdown for updating field.
field_vari = tk.StringVar(value="Student Name")
tk.Label(stud, text="Field to Update", bg = "#f4e6cb").pack(pady=5)
fieldOptions = ["Student Name", "Total Coursework", "Exam Mark"]
for option in fieldOptions:
    ttk.Radiobutton(stud, text=option, variable=field_vari, value=option).pack(pady=2)

# Dropdown to select a student name.
studDropwn = ttk.Combobox(stud, values=[], state="readonly")
studDropwn.pack(pady=10)

# A frame to display the student records.
resultFrame = tk.Frame(stud)
resultFrame.pack(pady=5, fill=tk.BOTH, expand=True)

# Displays the student record list inside the text box area.
displayText = tk.Text(resultFrame, height=15, bg = "#f4e6cb", wrap=tk.WORD, font=("Arial", 12))
displayText.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Displays a text box to view the student record.
scrollBar = tk.Scrollbar(resultFrame, command=displayText.yview)
scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
displayText.config(yscrollcommand=scrollBar.set)# Allows scrolling to view all record text.

# Loads the student marks file.
studentZ = loadStud_data('/Users/geronimojo/Desktop/studentMarks.txt')
# Calls the function to update the student record.
stud_dropwnUpdate()


# Runs the whole student manager program.
stud.mainloop()