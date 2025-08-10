import tkinter as tk
from tkinter import messagebox

class AIGuesserApp:
    def __init__(self, master):
        self.master = master
        self.master.title("AI Number Guesser")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        self.low = 1
        self.high = 100
        self.guess = None

        self.label = tk.Label(master, text="Think of a number between 1 and 100", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.guess_label = tk.Label(master, text="", font=("Helvetica", 20, "bold"))
        self.guess_label.pack(pady=20)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.higher_button = tk.Button(self.button_frame, text="Higher", width=10, command=self.higher)
        self.higher_button.grid(row=0, column=0, padx=5)

        self.correct_button = tk.Button(self.button_frame, text="Correct", width=10, command=self.correct)
        self.correct_button.grid(row=0, column=1, padx=5)

        self.lower_button = tk.Button(self.button_frame, text="Lower", width=10, command=self.lower)
        self.lower_button.grid(row=0, column=2, padx=5)

        self.restart_button = tk.Button(master, text="Restart", command=self.restart)
        self.restart_button.pack(pady=10)

        self.make_guess()

    def make_guess(self):
        if self.low > self.high:
            messagebox.showerror("Oops!", "You might have made a mistake. Let's restart!")
            self.restart()
            return

        self.guess = (self.low + self.high) // 2
        self.guess_label.config(text=f"My guess is: {self.guess}")

    def higher(self):
        self.low = self.guess + 1
        self.make_guess()

    def lower(self):
        self.high = self.guess - 1
        self.make_guess()

    def correct(self):
        messagebox.showinfo("Yay!", f"I guessed it! Your number is {self.guess} 🎉")
        self.restart()

    def restart(self):
        self.low = 1
        self.high = 100
        self.make_guess()

if __name__ == "__main__":
    root = tk.Tk()
    app = AIGuesserApp(root)
    root.mainloop()
