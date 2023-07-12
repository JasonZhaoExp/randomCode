import tkinter as tk

def calculate(event=None):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2

        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the input fields and labels
entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()
entry2.bind("<Return>", calculate)  # Bind the calculate function to the "Return" key being pressed

# Create the operation radio buttons
operation_var = tk.StringVar()
operation_var.set('+')

addition_radio = tk.Radiobutton(window, text='+', variable=operation_var, value='+')
addition_radio.pack()

subtraction_radio = tk.Radiobutton(window, text='-', variable=operation_var, value='-')
subtraction_radio.pack()

multiplication_radio = tk.Radiobutton(window, text='*', variable=operation_var, value='*')
multiplication_radio.pack()

division_radio = tk.Radiobutton(window, text='/', variable=operation_var, value='/')
division_radio.pack()

# Create the result label
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Start the main event loop
window.mainloop()