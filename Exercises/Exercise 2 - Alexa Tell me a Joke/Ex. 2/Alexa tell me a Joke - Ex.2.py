#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alexa tell me a Joke, Ex.2

Created on Sun Oct 27 16:24:31 2024

@author: geronimojo
"""
# Imports the all modules and functions of the tkinter GUI toolkit from Python's Library.
from tkinter import *
# Imports random module that generates random numbers taken from the Library.
import random
# Imports the os module for file handling.
import os

# Creates the main window.
fun = Tk() # Initializes the GUI toolkit.
fun.title("Alexa, tell me a Joke, Ex.2") # Creates a title
fun.configure(bg = "#F7F1A8") # Sets background color.
fun.resizable(width = False, height = False) # fixed window size.
fun.geometry('600x500') # Sets the window's width and height.

# Generates the jokes from the file given.
def loadingJokes(filePath):
    if not os.path.isfile(filePath): # Verifies file existence.
        return [] # Retrieves an empty list.
    with open(filePath, 'r') as file: # Accesses file in read mode.
        return [jokez.strip() for jokez in file.readlines()] # Reads and neatly sets up each line.


# Creates a random generated joke setup.
def shareJokes():
    jokez = random.choice(joke) # Selects a random joke from the file.
    setup, shareJokes.punchLine = jokez.split("?", 1) # Divides the joke into setup and punchline.
    joketxt.delete(1.0,END) # Empties the text area.
    joketxt.insert(END, setup + "?") # Displays setup.
    punchlineBttn.config(state = "normal") # The punchline button is enabled.

# Displays the joke's punchline.
def setPunchline(): 
    joketxt.insert(END,"\n\n" + shareJokes.punchLine.strip()) # Inserts the punchline in the text area.
    punchlineBttn.config(state = "disabled") # Disables the punchline button after the punchline being displayed.
    
# The user interface of the window is created.
def userInt():
    # Sets the main frame of the jokes generator.
    jokeFrame = Frame(fun, bg = "#F7F1A8") 
    jokeFrame.pack(pady = 20, fill = BOTH)
    
    # Displays the main title.
    joketitle = Label(jokeFrame, text = "Random Joke Generator", bg = "#F7F1A8", font = ("Times New Roman", 30), fg = "#51495b")
    joketitle.pack(pady = 10)
    
    # Modifies the style of the setup and punchline joke texts.
    global joketxt
    joketxt = Text(jokeFrame, height = 8, width = 40, bg = "#F7F1A8", font = ("Times New Roman", 20), fg = "#51495b")
    joketxt.pack(pady = 10)
    
    # The button that generates a new joke.
    shareJokesBttn = Button(jokeFrame, text="Alexa, tell me a Joke ଘ(੭*ˊᵕˋ)੭* ੈ♡‧₊˚""",  bg = "#F4CB7C", fg = "#51495b", font = ("Times New Roman", 20), command = shareJokes)
    shareJokesBttn.pack(pady = 5)
    
    # The button that generates the punchline and disables.
    global punchlineBttn
    punchlineBttn = Button(jokeFrame, text = "Show Punchline ⋆˚ʚɞ", state = "disabled", bg = "#F4CB7C", fg = "#51495b", font = ("Times New Roman", 20), command = setPunchline)
    punchlineBttn.pack(pady = 5)
    
    # The button that ends the random joke generator.
    quitBttn = Button(jokeFrame, text = "Quit", bg = "#F4CB7C", fg = "#51495b", font = ("Times New Roman", 17), command = fun.quit)
    quitBttn.pack(pady = 10)

# The jokes taken from the mentioned file path above.    
jokiefile = "/Users/geronimojo/Desktop/randomJokes.txt"
joke = loadingJokes(jokiefile)

# Calls the userInt function to set the window's user interface.
userInt()

# Operates the program as a loop.    
fun.mainloop()
        