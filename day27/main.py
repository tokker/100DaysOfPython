from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(200, 100)
window.config(padx=30, pady=30)

my_label1 = Label(text="Miles", font=("Arial", 12, "normal"))
my_label1.grid(row=0, column=2)

my_label2 = Label(text="is equal to", font=("Arial", 12, "normal"))
my_label2.grid(row=1, column=0)

my_label3 = Label(text="0", font=("Arial", 12, "normal"))
my_label3.grid(row=1, column=1)

my_label4 = Label(text="km", font=("Arial", 12, "normal"))
my_label4.grid(row=1, column=2)

def button_clicked():
    my_label3["text"] = round(float(input.get()) * 1.609)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2, column=1)

input = Entry(width=20)
input.focus()
input.grid(row=0, column=1)




window.mainloop()