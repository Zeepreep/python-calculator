#CALCULATOR FILE

from locale import resetlocale
import tkinter as tk

# importing the tkinter module, this is used to give the calculator its user-interface and create working buttons.

calculation = ""

def add_to_calculation(symbol):
    global calculation # making calculation a global variable, so that it can be manipulated inside of this function.
    calculation += str(symbol) # putting the symbol, which are the inserted numbers, into the calculation variable by making it a string.
    text_result.delete(1.0, "end") # clearing the calculator typing field, so that the answer can be put in the calculation's place.
    text_result.insert(1.0, calculation) # placing the answer to the calculation where the calculation used to be.



def evaluate_calculation():
    global calculation
    try: # a try is used here to see if the calculation can be performed, if it can not it will go to the except statement.
        calculation = str(eval(calculation)) # evaluates the equation entered to see if it can be done, if it can not it will return a false, which will activate the except statement.
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except: # since the calculation can not be done, this is used to display an error message.
        clear_field() # calls upon the clear_field method, which clears the calculation text box.
        text_result.insert(1.0, "Error") # inserts an error message in to the text box, to make it clear that the calculation can not be performed.

def clear_field():
    global calculation
    calculation = "" # makes sure the calculation function is empty.
    text_result.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x275")

# creating the root window, this is the window that will contain the calculator.

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# setting the right parameters for how the calculator will look. This creates 5 columns that the buttons can be places along, this is used to easily align them later.

btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)

# creating the button for the number 1. First of all the text is set to display the number, which is 1 in this case.
# The button then has a command. This command uses a Lambda expression, this is done so that the function is not immediately called. By using the Lambda expression the function is only called when the button is pressed.
# Then the number that is pressed is added into the calculation, this adds the number into the string that the calculation will use to solve the equation.
# After this the width and font of the button are declared so that the button will display correctly.
# Finally the button is placed in the correct row and column, this is done by using the grid function.
# The same is then done for most of the other buttons.

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_multiplication = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_multiplication.grid(row=4, column=4)
btn_division = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_division.grid(row=5, column=4)
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)

# Creating the buttons for the operators, these are all the same as the number buttons, except that they have a different text, and a different command.
btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)

# Creating the clear button, instead of adding to calculation, this button once again calls the clear field function.
# Another difference is that it spans 2 columns instead of 1.

btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=2)

# Creating the equals button, this button calls the evaluate calculation function, which evaluates the calculation.
# This button also spans 2 columns instead of 1.

root.mainloop()

# This is the last line of code, this is used to start the main loop of the program, this is what makes the program run.