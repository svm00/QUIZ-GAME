import tkinter as tk
import random

class MathQuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz Game")
        self.root.configure(bg="#34495e")  # Set the background color of the window
        self.score = 0
        self.question_count = 0
        self.create_widgets()
        self.next_question()

    def create_widgets(self):
        # Create a stylish label for the question
        self.question_label = tk.Label(self.root, text="", font=("Helvetica", 20, "bold"), fg="#ecf0f1", bg="#34495e",width=80)
        self.question_label.pack(pady=100)

        self.option_buttons = []
        for i in range(4):
            # Create stylish buttons for the answer options
            button = tk.Button(self.root, text="", font=("Helvetica", 16), width=40, height=2, 
                               bg="#3498db", fg="white", activebackground="#2980b9", activeforeground="white",
                               command=lambda i=i: self.check_answer(i))
            button.pack(pady=10)
            self.option_buttons.append(button)

        # Create a label to provide feedback after each answer
        self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 18), fg="#e74c3c", bg="#34495e")
        self.feedback_label.pack(pady=20)

        # Create a label to display the current score
        self.score_label = tk.Label(self.root, text="Score: 0", font=("Helvetica", 18, "bold"), fg="#2ecc71", bg="#34495e")
        self.score_label.pack(pady=20)

    def generate_question(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-", "*", "/"])
        if operation == "+":
            correct_answer = num1 + num2
        elif operation == "-":
            correct_answer = num1 - num2
        elif operation == "*":
            correct_answer = num1 * num2
        elif operation == "/":
            num1 *= num2  # Ensure division results in an integer
            correct_answer = num1 // num2

        question_text = f"{num1} {operation} {num2} = ?"
        options = [correct_answer,
                   correct_answer + random.randint(-10, 10),
                   correct_answer + random.randint(-10, 10),
                   correct_answer + random.randint(-10, 10)]
        random.shuffle(options)
        return question_text, correct_answer, options

    def next_question(self):
        if self.question_count < 10:
            self.question_count += 1
            self.question_text, self.correct_answer, self.options = self.generate_question()
            self.question_label.config(text=f"Q{self.question_count}: {self.question_text}")
            for i in range(4):
                self.option_buttons[i].config(text=str(self.options[i]))
            self.feedback_label.config(text="")
        else:
            self.end_quiz()

    def check_answer(self, selected_index):
        selected_answer = self.options[selected_index]
        if selected_answer == self.correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="#2ecc71")  # Green color for correct answers
        else:
            self.feedback_label.config(text=f"Incorrect! The correct answer was {self.correct_answer}.", fg="#e74c3c")  # Red color for incorrect answers
        self.score_label.config(text=f"Score: {self.score}")
        self.root.after(1000, self.next_question)

    def end_quiz(self):
        self.question_label.config(text="Quiz Over!")
        for button in self.option_buttons:
            button.pack_forget()
        self.feedback_label.config(text=f"Final Score: {self.score} out of 10", fg="#3498db")
        if self.score == 10:
            self.feedback_label.config(text=f"CONGRATULATIONS TOPPER!!!!",font=("Helvetica", 18, "bold") ,fg="#3498db",)


if __name__ == "__main__":
    root = tk.Tk()
    game = MathQuizGame(root)
    root.mainloop()
