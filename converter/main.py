from tkinter import *

# Create a window

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=50, height=20)
window.config(padx=10, pady=20)

# Entry to enter the value of miles

value = Entry(width=10)
value.insert(END, "Your value")
value.grid(column=1, row=0)

# Now Label

miles = Label(text="Miles")
miles.grid(column=2, row=0)

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

km = Label(text="km")
km.grid(column=2, row=1)

result = Label(text="0")
result.grid(column=1, row=1)


# Button for Calculate

def perform_calculation():
    answer = int(value.get())
    final_ans = answer * 1.609
    result.config(text=f"{final_ans}")


button = Button(text="Calculate", command=perform_calculation)
button.grid(column=1, row=2)

window.mainloop()
