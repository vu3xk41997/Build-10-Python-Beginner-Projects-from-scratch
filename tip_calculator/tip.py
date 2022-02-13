from tkinter import Tk, Radiobutton, Button, Label, StringVar, IntVar, Entry

# create class
class TipCalculator():
    def __init__(self):
        # create application window
        window = Tk()
        window.title("Tip Calculator App")
        window.configure(background="light gray")
        window.geometry("400x250")
        window.resizable(width=False, height=False)
    
        # create variables
        self.meal_cost = StringVar()
        self.tip_percentage = IntVar()
        self.tip_amount = StringVar()
        self.total_cost = StringVar()

        # create labels
        tip_percents = Label(window, text = "Tip Percentages", bg="dark gray", fg="white")
        tip_percents.grid(column=0, row=0, padx=15)

        bill_amount_lbl = Label(window, text = "Bill Amount", bg="light blue", fg="black")
        bill_amount_lbl.grid(column=1, row=0, padx=15)
        
        bill_amount_entry = Entry(window, textvariable=self.meal_cost, width=14)
        bill_amount_entry.grid(column=2, row=0)

        tip_amount_lbl = Label(window, text="Tip Amount", bg="blue", fg="white")
        tip_amount_lbl.grid(column=1, row=3, padx=15)

        tip_amount_entry = Entry(window, textvariable=self.tip_amount, width=14)
        tip_amount_entry.grid(column=2, row=3)

        total_cost_lbl = Label(window, text="Total Cost", bg="dark blue", fg="white")
        total_cost_lbl.grid(column=1, row=5, padx=15)

        total_cost_entry = Entry(window, textvariable=self.total_cost, width=14)
        total_cost_entry.grid(column=2, row=5)

        # create Radiobuttons
        five_percent_tip = Radiobutton(window, text="5%", variable=self.tip_percentage, value=5)
        five_percent_tip.grid(column=0, row=1)

        ten_percent_tip = Radiobutton(window, text="10%", variable=self.tip_percentage, value=10)
        ten_percent_tip.grid(column=0, row=2)

        fifteen_percent_tip = Radiobutton(window, text="15%", variable=self.tip_percentage, value=15)
        fifteen_percent_tip.grid(column=0, row=3)

        twenty_percent_tip = Radiobutton(window, text="20%", variable=self.tip_percentage, value=20)
        twenty_percent_tip.grid(column=0, row=4)

        twentyfive_percent_tip = Radiobutton(window, text="25%", variable=self.tip_percentage, value=25)
        twentyfive_percent_tip.grid(column=0, row=5)

        thirty_percent_tip = Radiobutton(window, text="30%", variable=self.tip_percentage, value=30)
        thirty_percent_tip.grid(column=0, row=6)

        # create calculate button
        calculate_button = Button(window, text="Calculate", bg="black", fg="black", command=self.calculate)
        calculate_button.grid(column=1, row=7, padx=15)

        # create clear button
        clear_button = Button(window, text="Clear", bg="black", fg="black", command=self.clear)
        clear_button.grid(column=2, row=7)

        window.mainloop()

    def calculate(self):
        pre_tip = float(self.meal_cost.get())
        percentage = self.tip_percentage.get() / 100
        tip_amount_entry = pre_tip * percentage
        self.tip_amount.set(tip_amount_entry)

        final_bill = pre_tip + tip_amount_entry
        self.total_cost.set(final_bill)

    def clear(self):
        self.meal_cost.set("")
        self.tip_amount.set("")
        self.total_cost.set("")
        
# run the class
TipCalculator()