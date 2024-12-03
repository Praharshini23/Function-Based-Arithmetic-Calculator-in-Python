import tkinter as tk

# Function to update the text entry with the button click
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

# Function to calculate the result
def calculate_result():
    try:
        result = eval(entry.get())  # Evaluate the expression entered by the user
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))  # Display the result in the entry field
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # Display error if invalid expression

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Basic Calculator")
window.geometry("400x600")

# Create a frame to hold the widgets
frame = tk.Frame(window, bg="blue", width=400, height=600, relief="raised")
frame.pack(fill="both", expand=True)

# Create an entry field to display the expression or result
entry = tk.Entry(frame, font=("Arial", 20), bd=10, relief="sunken", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Create number and operator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Place the buttons on the grid
for (text, row, column) in buttons:
    button = tk.Button(frame, text=text, font=("Arial", 18), relief="raised", bd=5, 
                       command=lambda value=text: button_click(value) if value != "=" and value != "C" else (calculate_result() if value == "=" else clear_entry()))
    button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)

# Configure grid to make buttons expand to fill space
for row in range(5):
    frame.grid_rowconfigure(row, weight=1)
for col in range(4):
    frame.grid_columnconfigure(col, weight=1)

# Run the Tkinter main loop
window.mainloop()
