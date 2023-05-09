'''
import tkinter as tk

# create a new window
window = tk.Tk()

# set the window size
window.geometry("800x600")

# set the window background color to black
window.configure(bg="black")

# set the font and text
font = ("Arial", 36)
text = "Hello, World!"

# create a label with the text
label = tk.Label(window, text=text, font=font, fg="white", bg="black")

# center the label in the window
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# run the window loop
window.mainloop()
'''

# ask for two numbers with commas
number1_input = input("Enter the first number with commas: ")
number2_input = input("Enter the second number with commas: ")

# remove commas from the input strings
number1_input = number1_input.replace(",", "")
number2_input = number2_input.replace(",", "")

# convert the input strings to floats and perform the calculation
result = float(number1_input) + float(number2_input)

# print the result
print(result)
