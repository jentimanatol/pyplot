import tkinter as tk
from tkinter import messagebox

# List of all questions and options
questions = [
    {
        "question": "For the population, find the proportion of even numbers. (Round to three decimal places as needed.)",
        "options": ["0.333", "0.500", "0.250", "0.125"],
        "answer": "0.333"
    },
    {
        "question": "The value of ModifyingAbove p with caret is?",
        "options": ["the margin of error", "the sample proportion", "the sample size", "found from evaluating 1 minus ModifyingAbove p with caret"],
        "answer": "the sample proportion"
    },
    # Add all remaining 55 questions similarly here.
]

# Quiz Application
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.current_question = 0
        self.score = 0

        # GUI Components
        self.question_label = tk.Label(self.root, text="", wraplength=500, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.options_frame = tk.Frame(self.root)
        self.options_frame.pack()

        self.options = []
        for i in range(4):  # Assuming 4 options per question
            rb = tk.Radiobutton(
                self.options_frame, text="", value=i, variable=tk.IntVar(), wraplength=400,
                font=("Arial", 12), anchor="w"
            )
            rb.grid(row=i, column=0, sticky="w")
            self.options.append(rb)

        self.next_button = tk.Button(
            self.root, text="Next", command=self.next_question,
            font=("Arial", 12), bg="#4CAF50", fg="white", width=10
        )
        self.next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        """Load the current question and options."""
        if self.current_question < len(questions):
            q = questions[self.current_question]
            self.question_label.config(text=f"Q{self.current_question + 1}: {q['question']}")
            for i, option in enumerate(q["options"]):
                self.options[i].config(text=option)
        else:
            self.end_quiz()

    def next_question(self):
        """Handle the next question button click."""
        selected_option = None
        for i, rb in enumerate(self.options):
            if rb.cget("text") == questions[self.current_question]["answer"]:
                selected_option = rb.cget("text")

        if selected_option == questions[self.current_question]["answer"]:
            self.score += 1

        self.current_question += 1
        if self.current_question < len(questions):
            self.load_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        """End the quiz and show the score."""
        messagebox.showinfo("Quiz Completed", f"You've completed the quiz!\nYour score is: {self.score}/{len(questions)}")
        self.root.destroy()


# Run the Quiz Application
if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizApp(root)
    root.mainloop()