import tkinter as tk
from tkinter import scrolledtext
import datetime
import webbrowser

def process_command():
    user_input = entry.get().strip().lower()
    print("fnction is running   ")

    if not user_input:
        return

    chat_window.insert(tk.END, f"\nYou: {user_input}\n")
    entry.delete(0, tk.END)

    if "hello" in user_input or "hi" in user_input:
        response = "Hello sir! How can I assist you?"

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = "Current time is " + current_time

    elif "date" in user_input:
        today = datetime.date.today()
        response = "Today's date is " + str(today)

    elif "open google" in user_input:
        webbrowser.open("https://www.google.com")
        response = "Opening Google..."

    elif "open youtube" in user_input:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube..."

    elif user_input.startswith("search"):
        query = user_input.replace("search", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            response = f"Searching for '{query}'..."
        else:
            response = "Please tell me what to search."

    elif "calculate" in user_input:
        try:
            expression = user_input.replace("calculate", "").strip()
            result = eval(expression, {"__builtins__": None}, {})
            response = "Result = " + str(result)
        except:
            response = "Invalid calculation."

    elif "bye" in user_input:
        response = "Goodbye sir!"
        chat_window.insert(tk.END, "Assistant: " + response + "\n")
        root.after(1000, root.destroy)
        return

    else:
        response = "I don't understand that."

    chat_window.insert(tk.END, "Assistant: " + response + "\n")
    chat_window.yview(tk.END)


# Create Window
root = tk.Tk()
root.title("Smart Assistant")
root.geometry("500x500")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root)
entry.pack(padx=10, pady=5, fill=tk.X)

send_button = tk.Button(root, text="Send")
send_button.config(command=process_command)
send_button.pack(pady=5)
root.bind('<Return>', lambda event: process_command())

root.mainloop()