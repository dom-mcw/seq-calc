import math
import tkinter as tk

def calculate_sequence():
    sequence_type = sequence_type_var.get()
    try:
        n = float(num_terms_entry.get())
        a = float(first_term_entry.get())
        a2 = float(second_term_entry.get())
        
        if sequence_type == 'A':  # Arithmetic sequence
            d = a2 - a  # find the common difference
            result = a + (n - 1) * d  # Arithmetic sequence formula
        elif sequence_type == 'G':  # Geometric sequence
            r = a2 / a  # find the common ratio
            result = a * pow(r, n - 1)  # Geometric sequence formula
        else:
            result = None
        
        if result is not None:
            result_label.config(text=f"Result: {round(result, 5)}")
        else:
            result_label.config(text="Invalid sequence type.")
    except ValueError:
        result_label.config(text="Invalid input. Enter a number.")

# Create the main window
window = tk.Tk()
window.title("Sequence Calculator")

# Create the GUI components
sequence_type_label = tk.Label(window, text="Enter the type of sequence: 'A' or 'G': ")
sequence_type_label.pack()
sequence_type_var = tk.StringVar()
sequence_type_entry = tk.Entry(window, textvariable=sequence_type_var)
sequence_type_entry.pack()

num_terms_label = tk.Label(window, text="Enter the number of terms in the sequence: ")
num_terms_label.pack()
num_terms_entry = tk.Entry(window)
num_terms_entry.pack()

first_term_label = tk.Label(window, text="Enter the first term in the sequence: ")
first_term_label.pack()
first_term_entry = tk.Entry(window)
first_term_entry.pack()

second_term_label = tk.Label(window, text="Enter the second term in the sequence: ")
second_term_label.pack()
second_term_entry = tk.Entry(window)
second_term_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_sequence)
calculate_button.pack()

result_label = tk.Label(window)
result_label.pack()

# Run the main event loop
window.mainloop()
