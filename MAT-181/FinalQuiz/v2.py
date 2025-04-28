import tkinter as tk
from tkinter import messagebox

# List of questions and answers (replace placeholders with actual questions)
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
    # Add all other 55 questions here in the same format
]

# Quiz Application Class
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.current_question_index = 0
        self.score = 0

        # Question Frame
        self.question_label = tk.Label(root, text="", wraplength=500, font=("Arial", 14))
        self.question_label.pack(pady=20)

        # Options Frame
        self.options_var = tk.StringVar()  # Variable to hold the selected option
        self.options_frame = tk.Frame(root)
        self.options_frame.pack()

        self.options_buttons = []
        for i in range(4):  # Assuming each question has 4 options
            rb = tk.Radiobutton(
                self.options_frame, text="", variable=self.options_var, value="", font=("Arial", 12), anchor="w"
            )
            rb.grid(row=i, column=0, sticky="w")
            self.options_buttons.append(rb)

        # Next Button
        self.next_button = tk.Button(
            root, text="Next", command=self.next_question, font=("Arial", 12), bg="#4CAF50", fg="white", width=10
        )
        self.next_button.pack(pady=10)

        # Load the first question
        self.load_question()

    def load_question(self):
        """Load the current question and its options."""
        if self.current_question_index < len(questions):
            question_data = questions[self.current_question_index]
            self.question_label.config(text=f"Q{self.current_question_index + 1}: {question_data['question']}")

            # Update options
            for i, option in enumerate(question_data["options"]):
                self.options_buttons[i].config(text=option, value=option)
                self.options_var.set(None)  # Reset selected option
        else:
            self.end_quiz()

    def next_question(self):
        """Handle the next question button click."""
        selected_option = self.options_var.get()
        if selected_option == questions[self.current_question_index]["answer"]:
            self.score += 1

        self.current_question_index += 1
        self.load_question()

    def end_quiz(self):
        """End the quiz and display the score."""
        messagebox.showinfo("Quiz Completed", f"You've completed the quiz!\nYour score is: {self.score}/{len(questions)}")
        self.root.destroy()


# Run the Quiz Application
if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizApp(root)
    root.mainloop()