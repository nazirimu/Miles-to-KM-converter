import tkinter


# Converts miles to kilometers when button is clicked
def convert_button():
    # retrieves the input
    miles_input = float(input.get())
    # Calculates the km from the output
    km_output = round(miles_input * 1.609, 2)
    # Displays the output on the screen
    output_label.config(text=f"{km_output}")


# Setting up the window
window = tkinter.Tk()
window.minsize(width=300, height=150)
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)

# input box
input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

# miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

# is equals to label
equals_label = tkinter.Label(text="is equal to")
equals_label.grid(column=0, row=1)

# Km label
km_label = tkinter.Label(text="km")
km_label.grid(column=2, row=1)

# output label
output_label = tkinter.Label(text="0", font=("bold"))
output_label.grid(column=1, row=1)

# Button
button = tkinter.Button(text="Convert", command=convert_button)
button.grid(column=1, row=2)

# Keeps the Window open and listening to commands
window.mainloop()
