import random
import tkinter as tk

class GuessTheNumber:
    def __init__(self, master):
        self.master = master
        master.title("Guess the Number")

        # Set the minimum and maximum values for the random number
        self.min_number = 1
        self.max_number = 100

        # Generate a random number between the minimum and maximum values
        self.secret_number = random.randint(self.min_number, self.max_number)

        # Set the number of attempts allowed for the player
        self.max_attempts = 10
        self.remaining_attempts = self.max_attempts

        # Create the GUI elements
        self.label1 = tk.Label(master, text="Guess the number between " + str(self.min_number) + " and " + str(self.max_number))
        self.label1.pack()

        self.entry1 = tk.Entry(master)
        self.entry1.pack()

        self.button1 = tk.Button(master, text="Guess", command=self.guess_number)
        self.button1.pack()

        self.label2 = tk.Label(master, text="You have " + str(self.remaining_attempts) + " attempts remaining")
        self.label2.pack()

        self.label3 = tk.Label(master, text="")
        self.label3.pack()

    def guess_number(self):
        guess = int(self.entry1.get())

        if guess == self.secret_number:
            self.label3.config(text="Congratulations! You guessed the number in " + str(self.max_attempts - self.remaining_attempts + 1) + " attempts.")
            self.button1.config(state="disabled")
        else:
            self.remaining_attempts -= 1
            self.label2.config(text="You have " + str(self.remaining_attempts) + " attempts remaining")

            if self.remaining_attempts == 0:
                self.label3.config(text="Sorry, you ran out of attempts. The correct number was " + str(self.secret_number) + ".")
                self.button1.config(state="disabled")
            elif guess < self.secret_number:
                self.label3.config(text="Too low. Try again.")
            elif guess > self.secret_number:
                self.label3.config(text="Too high. Try again.")

# Create the main window and run the game
root = tk.Tk()
game = GuessTheNumber(root)
root.mainloop()
