"""
1/9/2023 Program: numberGuessGUI2.py

Chapter 8 case study: GUI based version of the number guess game from chapter 3 Modified

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

ALSO NOTE: you MUST install the pygame package by running: pip install pygame
"""

from breezypythongui import EasyFrame
import random
from tkinter.font import Font
from pygame import mixer
from tkinter import PhotoImage
# Other imports can go here

class GuessingGame(EasyFrame):

	# Definition of the __init__() method which is our class constructor
	def __init__(self):
		# Call the EasyFrame constructor method
		EasyFrame.__init__(self, title = "Homer's Guessing Game", background = "#FF89B8", width = 720, height = 680)

		# initialize instance varaibles for the class
		self.magicNum = random.randint(1, 100)
		self.count = 0

		# fonts
		font1 = Font(family = "Modern", size = 14, weight = "bold")
		font2 = Font(family = "Comic Sans MS", size = 26, weight = "bold")
		font3 = Font(family = "Modern", size = 18, weight = "bold")

		# create and add header label, image label, and instruction label to the window
		self.header = self.addLabel(text = "LET'S PLAY A GUESSING GAME !", row = 0, column = 0, columnspan = 2, sticky = "NESW", background = "#FF89B8")
		self.header["font"] = font2
		self.header["foreground"] = "#FFF838"
		self.img = self.addLabel(text = "", row = 2, column = 0, columnspan = 2, sticky = "NSEW", background = "#FF89B8")
		self.image = PhotoImage(file = "hsimpson.png")
		self.img["image"] = self.image
		self.instructions = self.addLabel(text = "GUESS HOMER'S NUMBER IN AS FEW TRIES AS POSSIBLE", row = 1, column = 0, columnspan = 2, sticky = "NESW", background = "#FF89B8")
		self.instructions["font"] = font1
		self.instructions["foreground"] = "#7DF7EC"
		# create and add hint label to the window
		self.hintLabel = self.addLabel(text = "Guess a number between 1 and 100", row = 3, column = 0, columnspan = 2, sticky = "NESW", background = "#FF89B8")
		self.hintLabel["font"] = font3
		self.hintLabel["foreground"] = "white"
		# create and add the guess label, and guess field
		self.guessLabel = self.addLabel(text = "Your guess:", row = 4, column = 0, background = "#FF89B8", sticky = "E")
		self.guessLabel["font"] = font3
		self.guessLabel["foreground"] = "#7DF7EC"
		self.guessField = self.addIntegerField(value = 0, row = 4, column = 1, sticky = "W", width = 5)
		self.guessField["bg"] = "Powder Blue"
		# create and add the guess button and new game button to the window
		self.guessButton = self.addButton(text = "GUESS", row = 5, column = 0, command = self.nextGuess)
		self.guessButton["font"] = "Modern"
		self.guessButton["bg"] = "#65C6BE"
		self.guessButton["fg"] = "black"
		self.guessButton["bd"] = 3
		self.guessButton["width"] = 25
		self.newButton = self.addButton(text = "NEW GAME", row = 5, column = 1, command = self.newGame)
		self.newButton["font"] = "Modern"
		self.newButton["bg"] = "#65C6BE"
		self.newButton["fg"] = "black"
		self.newButton["bd"] = 3
		self.newButton["width"] = 25

	# Definition of the event handling methods for this class
	def nextGuess(self):
		""" Processes the users next guess """
		self.count += 1
		userNum = self.guessField.getNumber()
		# Logic that determines the games outcome
		if userNum < self.magicNum:
			self.hintLabel["text"] = "Sorry, your guess was too small!"
		elif userNum > self.magicNum:
			self.hintLabel["text"] = "Sorry, your guess was too large!"
		else:
			self.hintLabel["text"] = "Congratulations! You got it in " + str(self.count) + " tries!"
			self.guessButton["state"] = "disabled"
			mixer.init()
			mixer.Sound(file = "win.mp3").play()

	def newGame(self):
		""" Resets the data in GUI back to their original states """
		self.magicNum = random.randint(1, 100)
		self.count = 0
		self.hintLabel["text"] = "Guess a number between 1 and 100"
		self.guessField.setNumber(0)
		self.guessButton["state"] = "normal"

# Definition of the main() method which will establish class objects
def main():
	# Instantiate an object from the class into mainloop()
	GuessingGame().mainloop()

# Global call to the main() method
main()