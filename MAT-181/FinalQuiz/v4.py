import tkinter as tk
from tkinter import messagebox

# List of all 57 questions
questions = [
    # Populate this list with each question mentioned in the conversation history
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
    {
        "question": "Find the critical value z Subscript alpha divided by 2 that corresponds to the given confidence level. 87%",
        "options": ["1.81", "1.23", "1.56", "2.01"],
        "answer": "1.81"
    },
    {
        "question": "Express the confidence interval 0.666 < p < 0.888 in the form ModifyingAbove p with caret plus or minus Upper E.",
        "options": ["0.777 ± 0.111", "0.700 ± 0.111", "0.750 ± 0.120", "0.800 ± 0.100"],
        "answer": "0.777 ± 0.111"
    },
    {
        "question": "What is the confidence interval estimate of the mean body temperature of all healthy humans?",
        "options": ["98.111°F < μ < 98.489°F", "98.200°F < μ < 98.600°F", "98.000°F < μ < 98.500°F", "98.050°F < μ < 98.450°F"],
        "answer": "98.111°F < μ < 98.489°F"
    },
    {
        "question": "What is the P-value for the test statistic z = -10.16?",
        "options": ["Approximately 0", "0.05", "0.01", "0.10"],
        "answer": "Approximately 0"
    },
    # Add the rest of the questions here (in the same format as above, with question, options, and the correct answer).
    # Repeat this structure for all 57 questions in the chat history.
]

# Quiz Application Class
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.current_question_index = 0
        self.user_answers = [None] * len(questions)  # Stores user's answers
        self.score = 0

        # Top Frame for Question Counter
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(pady=10)

        self.question_counter_label = tk.Label(self.top_frame, text=f"Question 1 of {len(questions)}", font=("Arial", 14))
        self.question_counter_label.pack()

        # Question Label
        self.question_label = tk.Label(root, text="", wraplength=500, font=("Arial", 14))
        self.question_label.pack(pady=20)

        # Options Frame
        self.options_var = tk.StringVar()
        self.options_frame = tk.Frame(root)
        self.options_frame.pack()

        self.options_buttons = []
        for i in range(4):  # Assuming each question has 4 options
            rb = tk.Radiobutton(
                self.options_frame, text="", variable=self.options_var, value="", font=("Arial", 12), anchor="w"
            )
            rb.grid(row=i, column=0, sticky="w")
            self.options_buttons.append(rb)

        # Navigation Buttons
        self.nav_frame = tk.Frame(root)
        self.nav_frame.pack(pady=20)

        self.back_button = tk.Button(
            self.nav_frame, text="Back", command=self.previous_question, font=("Arial", 12), bg="#f0ad4e", fg="white", width=10
        )
        self.back_button.grid(row=0, column=0, padx=10)

        self.next_button = tk.Button(
            self.nav_frame, text="Next", command=self.next_question, font=("Arial", 12), bg="#4CAF50", fg="white", width=10
        )
        self.next_button.grid(row=0, column=1, padx=10)

        # Load the first question
        self.load_question()

    def load_question(self):
        """Load the current question and update GUI components."""
        question_data = questions[self.current_question_index]
        self.question_label.config(text=f"Q{self.current_question_index + 1}: {question_data['question']}")
        self.question_counter_label.config(text=f"Question {self.current_question_index + 1} of {len(questions)}")

        for i, option in enumerate(question_data["options"]):
            self.options_buttons[i].config(text=option, value=option)
        
        # Set previously selected answer if it exists
        self.options_var.set(self.user_answers[self.current_question_index])

    def next_question(self):
        """Move to the next question."""
        # Save the current answer
        selected_option = self.options_var.get()
        if selected_option:
            self.user_answers[self.current_question_index] = selected_option

        # Move to the next question
        if self.current_question_index < len(questions) - 1:
            self.current_question_index += 1
            self.load_question()
        else:
            self.end_quiz()

    def previous_question(self):
        """Move to the previous question."""
        # Save the current answer
        selected_option = self.options_var.get()
        if selected_option:
            self.user_answers[self.current_question_index] = selected_option

        # Move to the previous question
        if self.current_question_index > 0:
            self.current_question_index -= 1
            self.load_question()

    def end_quiz(self):
        """End the quiz and calculate the score."""
        self.score = sum(
            1 for i, question in enumerate(questions)
            if self.user_answers[i] == question["answer"]
        )
        messagebox.showinfo(
            "Quiz Completed",
            f"You've completed the quiz!\nYour score is: {self.score}/{len(questions)}"
        )
        self.root.destroy()


# Run the Quiz Application
if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizApp(root)
    root.mainloop()