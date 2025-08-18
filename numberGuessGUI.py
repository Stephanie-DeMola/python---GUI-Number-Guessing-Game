"""
Program: numberGuessGUI.py
Chapter 9 Case Study (pgs. 242 - 245)
08/15/2025
Developer: Stephanie DeMola

***NOTE: the Python module breezypythongui.py MUST be in the sma edirectory as this file for the app to run properly!

GUI-based version of the number guessing game app from Chapter 3 _ ch3>numberGuess.py
"""
from breezypythongui import EasyFrame
from tkinter.font import Font
import random
# Other imports can go here

# Class Header (class name will change project to project)
class GuessingGame(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		"""Sets up the window and the widgets."""
		# Call to the EastFrame class constructor
		EasyFrame.__init__(self, title = "Guessing Game 2.0", width = 640, height = 500, background = "darkslateblue")
		# Create the instance variable for this class
		self.myNumber = random.randint(1, 100)
		self.count = 0
		# Add the widgets to that EasyFrame window
		self.hintLabels = self.addLabel(text = "Welcome to Number Guessing Game!", row = 0, column = 0, background = "darkslateblue", columnspan = 2, sticky = "NEWS", foreground = "spring green", font = Font(size = 24, family = "Stencil"))
		self.hintLabel = self.addLabel(text = "Guess a number between 1 and 100", row = 1, column = 0, background = "darkslateblue", columnspan = 2, sticky = "NEWS", foreground = "pale green", font = Font(size = 20, family = "Impact"))
		self.addLabel(text = "Give It Your Best Guess >>", row = 2 , column = 0, background = "darkslateblue", foreground = "pale green",font = Font(size = 14, family = "Impact"))
		self.guessField = self.addIntegerField(value = 0, row = 2, column = 1, width = 20)
		# Bind additional keys to the input that can also trigger nextGuess()
		self.guessField.bind("<Return>", lambda event: self.nextGuess())
		self.guessField.bind("<space>", lambda event: self.nextGuess())
		self.guessField.focus_set()



		self.nextButton = self.addButton(text = "Guess", row = 3, column = 0, command = self.nextGuess)
		self.nextButton["width"] = 10
		self.nextButton["background"] = "spring green"
		self.nextButton["font"] = Font(size = 12, family = "Impact")
		self.newButton = self.addButton(text = "New Game", row = 3, column = 1, state = "disabled", command = self.newGame)
		self.newButton["width"] = 10
		self.newButton["background"] = "spring green"
		self.newButton["font"] = Font(size = 12, family = "Impact")


	# Definition of the nextGuess() method which handles the next button click
	def nextGuess(self):
		self.count += 1
		# Grab the user input from the IntegerField
		guess = self.guessField.getNumber()
		# Logic that determines the games outcome
		if guess == self.myNumber:
			self.hintLabel["text"] = f"Congrats! You got it in {self.count} attempt(s)"
			self.nextButton["state"] = "disabled"
			self.newButton["state"] = "normal"
		elif guess < self.myNumber:
			self.hintLabel["text"] = "Sorry! Your guess was too low."
		else:
			self.hintLabel["text"] = "Oops! Your guess was too high!"
	
	# Definition of the newGame() methods which handles the "new game" button click
	def newGame(self):
		# Resets the data and GUI to their original states
		self.myNumber = random.randint(1,100)
		self.count = 0
		self.hintLabel["text"] = "Guess a Number Between 1 and 100"
		self.guessField.setNumber(0)	
		self.nextButton["state"] = "normal"
		self.newButton["state"] = "disabled"
		
# End of class block


# Global definition of the main() function
def main():
	# Instantiate an object from the class into mainloop() **This is my INSTANCE**
	GuessingGame().mainloop()


# Global call to main() for program entry
	# ***THIS NEVER CHANGES FROM CODE TO CODE***
if __name__ == '__main__':
	main()


