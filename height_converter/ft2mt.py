# import module
from tkinter import Tk, Button, Label, DoubleVar, Entry

# create application window and add configuration
window = Tk()
window.title("Feet to Meter Converter App")
window.configure(background="light gray")
window.geometry("320x220")
window.resizable(width=False, height=False)

# convert funtion
def convert():
    value = float(ft_entry.get())
    meter = value * 0.3048
    mt_value.set("%.4f" % meter)

# clear function
def clear():
    ft_value.set("")
    mt_value.set("")

# create label and widget
# Feet label
ft_lbl = Label(window, text = "Feet", bg="pink", fg="black", width=14)
ft_lbl.grid(column=0, row=0, padx=15, pady=15)

# Feet entry widget
ft_value = DoubleVar()
ft_entry = Entry(window, textvariable=ft_value, width=14)
ft_entry.grid(column=1, row=0)
ft_entry.delete(0, "end")

# Meter label
mt_lbl = Label(window, text = "Meter", bg="orange", fg="black", width=14)
mt_lbl.grid(column=0, row=1)

# Meter entry widget
mt_value = DoubleVar()
mt_entry = Entry(window, textvariable=mt_value, width=14)
mt_entry.grid(column=1, row=1, pady=30)
mt_entry.delete(0, "end")

# create buttons
# convert button
convert_btn = Button(window, text="Convert", highlightbackground="light blue", fg="black", width=14, command=convert)
convert_btn.grid(column=0, row=3, padx=15)

# clear button
clear_btn = Button(window, text="Clear", highlightbackground="light green", fg="black", width=14, command=clear)
clear_btn.grid(column=1, row=3, padx=15)



window.mainloop()