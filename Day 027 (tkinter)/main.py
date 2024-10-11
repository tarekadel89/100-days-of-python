import tkinter as t

my_window = t.Tk()
my_window.title("Miles to Kilometers Calculator")
my_window.minsize(width=100, height=100)
my_window.config(padx= 25, pady=25)

mile_entry = t.Entry()
mile_entry.config(width=10)
mile_entry.insert(t.END, string="0")
mile_entry.grid(row=0, column=1)

miles_label = t.Label()
miles_label.config(text="Miles")
miles_label.grid(row=0, column=2)

isEqualTo_label = t.Label()
isEqualTo_label.config(text="is equal to")
isEqualTo_label.grid(row=1, column=0)

kmsVal_label = t.Label()
kmsVal_label.config(text="0.00")
kmsVal_label.grid(row=1, column=1)

kms_label = t.Label()
kms_label.config(text="kms")
kms_label.grid(row=1, column=3)

def convert_miles_to_kms():
    miles = float(mile_entry.get())
    kms = miles * 1.60934
    kmsVal_label.config(text=f"{kms:.2f}")

convert_button = t.Button()
convert_button.config(text="Convert", command=convert_miles_to_kms)
convert_button.grid(row=2, column=1)

my_window.mainloop() #