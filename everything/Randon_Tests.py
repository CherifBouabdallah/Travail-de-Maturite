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
