import json
import tkinter as tk
from tkinter import messagebox

# Load the JSON file containing questions
def load_questions(file_path):
    with open(file_path, 'r') as file:
        questions = json.load(file)
    return questions

# Quiz Application Class
class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.root.title("Student Quiz")
        self.questions = questions
        self.current_question_index = 0
        self.user_answers = [None] * len(questions)  # Track user answers
        self.score = 0

        # Header Frame for Title
        self.header_frame = tk.Frame(root, bg="#4CAF50")
        self.header_frame.pack(fill="x")
        self.title_label = tk.Label(
            self.header_frame, text="Welcome to the Quiz A Jentimir", font=("Arial", 24), bg="#4CAF50", fg="white", pady=10
        )
        self.title_label.pack()

        # Question Counter
        self.counter_label = tk.Label(root, text="", font=("Arial", 14))
        self.counter_label.pack(pady=10)

        # Question Frame
        self.question_label = tk.Label(root, text="", wraplength=600, font=("Arial", 16))
        self.question_label.pack(pady=20)

        # Options Frame
        self.options_var = tk.StringVar()
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=10)

        self.options_buttons = []
        for i in range(4):  # Assume each question has 4 options
            rb = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.options_var,
                value="",
                font=("Arial", 14),
                wraplength=500,
                anchor="w"
            )
            rb.pack(anchor="w", pady=5)
            self.options_buttons.append(rb)

        # Navigation Buttons
        self.navigation_frame = tk.Frame(root)
        self.navigation_frame.pack(pady=20)

        self.back_button = tk.Button(
            self.navigation_frame,
            text="Back",
            command=self.previous_question,
            font=("Arial", 12),
            bg="#f0ad4e",
            fg="white",
            state=tk.DISABLED,  # Disabled initially
            width=10
        )
        self.back_button.grid(row=0, column=0, padx=10)

        self.next_button = tk.Button(
            self.navigation_frame,
            text="Next",
            command=self.next_question,
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            width=10
        )
        self.next_button.grid(row=0, column=1, padx=10)

        self.submit_button = tk.Button(
            self.navigation_frame,
            text="Submit",
            command=self.end_quiz,
            font=("Arial", 12),
            bg="#2196F3",
            fg="white",
            width=10
        )
        self.submit_button.grid(row=0, column=2, padx=10)

        # Load the first question
        self.load_question()

    def load_question(self):
        """Load the current question and update GUI components."""
        question_data = self.questions[self.current_question_index]
        self.counter_label.config(
            text=f"Question {self.current_question_index + 1} of {len(self.questions)}"
        )
        self.question_label.config(text=question_data['question'])

        for i, option in enumerate(question_data['options']):
            self.options_buttons[i].config(text=option, value=option)
            self.options_var.set(self.user_answers[self.current_question_index])

        # Enable/disable navigation buttons
        self.back_button.config(state=tk.NORMAL if self.current_question_index > 0 else tk.DISABLED)
        self.next_button.config(state=tk.NORMAL if self.current_question_index < len(self.questions) - 1 else tk.DISABLED)

    def next_question(self):
        """Save answer and move to the next question."""
        self.save_answer()
        self.current_question_index += 1
        self.load_question()

    def previous_question(self):
        """Save answer and move to the previous question."""
        self.save_answer()
        self.current_question_index -= 1
        self.load_question()

    def save_answer(self):
        """Save the user's current answer."""
        selected_option = self.options_var.get()
        if selected_option:
            self.user_answers[self.current_question_index] = selected_option

    def end_quiz(self):
        """End the quiz, calculate the score, and display results."""
        self.save_answer()
        self.score = sum(
            1 for i, question in enumerate(self.questions)
            if self.user_answers[i] == question["answer"]
        )
        result_message = f"Quiz Completed!\nYour score is {self.score}/{len(self.questions)}"
        messagebox.showinfo("Quiz Results", result_message)
        self.show_review()

    def show_review(self):
        """Display a review of all answers."""
        review_window = tk.Toplevel(self.root)
        review_window.title("Quiz Review")
        review_frame = tk.Frame(review_window)
        review_frame.pack(pady=10, padx=10)

        for i, question in enumerate(self.questions):
            q_label = tk.Label(
                review_frame,
                text=f"Q{i + 1}: {question['question']}\n"
                     f"Your answer: {self.user_answers[i]}\n"
                     f"Correct answer: {question['answer']}\n",
                font=("Arial", 12),
                anchor="w",
                justify="left",
                wraplength=600
            )
            q_label.pack(anchor="w", pady=5)

        close_button = tk.Button(review_window, text="Close", command=review_window.destroy, font=("Arial", 12))
        close_button.pack(pady=10)

# Main Application
if __name__ == "__main__":
    # Load questions from JSON file
    questions = load_questions("quiz_questions.json")

    # Create the main window
    root = tk.Tk()
    app = QuizApp(root, questions)
    root.mainloop()