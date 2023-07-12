# This program is for the AI colab assignment. Brandon Kling 7/6/2023
# In this program I created a Magic 8 Ball program that will answer any question you ask it.

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import random

def get_random_answer():
    # List of possible answers from the Magic 8 Ball
    answers = [
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes – definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    # Randomly choose an answer from the list
    return random.choice(answers)

def ask_question():
    # Get the question from the entry field
    question = question_entry.get()
    if question:
        # Generate a random answer
        answer = get_random_answer()

        # Create a Toplevel window for the answer
        answer_window = tk.Toplevel(root)
        answer_window.title("Magic 8 Ball - Answer")
        answer_window.configure(bg="black")

        # Create a label to display the answer
        answer_label = tk.Label(answer_window, text=f"Question: {question}\n\nAnswer: {answer}", fg="white", bg="black", font=("Arial", 12))
        answer_label.pack(padx=20, pady=20)

        # Create a button to close the answer window
        close_button = tk.Button(answer_window, text="Close", command=lambda: close_answer(answer_window), bg="black", fg="white", font=("Arial", 12))
        close_button.pack(pady=10)

        # Clear the question entry box
        question_entry.delete(0, tk.END)

        # Center the answer window
        answer_window.withdraw()
        answer_window.update_idletasks()
        x = int((answer_window.winfo_screenwidth() - answer_window.winfo_width()) / 2)
        y = int((answer_window.winfo_screenheight() - answer_window.winfo_height()) / 2)
        answer_window.geometry(f"+{x}+{y}")
        answer_window.deiconify()
    else:
        # Display a warning if no question is entered
        messagebox.showwarning("Magic 8 Ball", "Please enter a question.")

# Function to close the answer window
def close_answer(window):
    window.destroy()

# Create the main window
root = tk.Tk()
root.title("Magic 8 Ball")

# Set the window size and position it in the center of the screen
window_width = 800
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Load the background image
image = Image.open("magic8ball.jpg")
image = image.resize((window_width, window_height), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image)

# Create a canvas to display the background image
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, anchor=tk.NW, image=background_image)

# Create a frame for the content with a black border
frame = tk.Frame(canvas, bg="black", bd=5, highlightbackground="white", highlightcolor="white", highlightthickness=2)
frame.place(relx=0.5, rely=0.5, relwidth=0.8, relheight=0.6, anchor=tk.CENTER)

# Create a label with the welcome message and add it to the frame
welcome_label = tk.Label(frame, text="Welcome to the Magic 8 Ball.\nHere you will ask questions to discover your true destiny.", fg="white", bg="black", font=("Arial", 18))
welcome_label.pack(pady=20)

# Create an entry field for the question and add it to the frame
question_entry = tk.Entry(frame, width=50, font=("Arial", 14))
question_entry.pack(pady=60)

# Create a button to ask the question and add it to the frame
ask_button = tk.Button(frame, text="Ask", command=ask_question, bg="black", fg="white", font=("Arial", 14))
ask_button.pack(pady=10)

# Start the main event loop
root.mainloop()