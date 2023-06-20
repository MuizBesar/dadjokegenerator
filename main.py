import requests
import json
import tkinter as tk

def fetch_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    joke = data["joke"]
    return joke

def generate_dad_joke():
    joke = fetch_joke()
    joke_label.config(text=joke)

# Create the main window
window = tk.Tk()
window.title("Dad Joke Generator")

# Create a label to display the joke
joke_label = tk.Label(window, text="Press the button to generate a joke!", wraplength=300)
joke_label.pack(pady=20)

# Create a button to generate a joke
generate_button = tk.Button(window, text="Generate Joke", command=generate_dad_joke)
generate_button.pack(pady=10)

# Run the main event loop
window.mainloop()
