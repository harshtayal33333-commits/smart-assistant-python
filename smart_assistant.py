import datetime
import webbrowser
import os

def show_help():
    print("""
Available Commands:
- hello / hi
- time
- date
- open google
- open youtube
- search <something>
- calculate
- help
- bye
""")

print("Smart Assistant Started!")
print("Type 'help' to see commands.\n")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Assistant: Hello sir  How can I assist you?")

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(" Assistant: Current time is", current_time)

    elif "date" in user_input:
        today = datetime.date.today()
        print(" Assistant: Today's date is", today)

    elif "open google" in user_input:
        print(" Assistant: Opening Google...")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in user_input:
        print(" Assistant: Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif user_input.startswith("search"):
        query = user_input.replace("search", "").strip()
        if query:
            print(f" Assistant: Searching for '{query}'...")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            print(" Assistant: Please tell me what to search.")
            
    elif "calculate" in user_input:
        try:
            expression = input("Enter calculation (example 5+3): ")
            result = eval(expression)
            print(" Assistant: Result =", result)
        except:
            print(" Assistant: Invalid calculation.")
    elif "help" in user_input:
        show_help()

    elif "bye" in user_input:
        print(" Assistant: Goodbye sir! ")
        break

    else:
        print(" Assistant: I don't understand that. Type 'help' to see commands.")
        
