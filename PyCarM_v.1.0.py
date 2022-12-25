# PyCarM_v.1.0.py

from show import *
from add import *
from sell import *
from change import *

window = Tk()

window.geometry("700x350")
window.title("PyCarM V.1.0")
frame = Frame(window, relief="ridge", borderwidth=5)
frame.pack(fill="both", expand=1)
button1 = Show(frame, text="Show all cars", width=20, height=5)
button1.config(font=("Arial", 12, "bold"))
button1["command"] = button1.show
button1.place(x=50, y=50)
button2 = Add(frame, text="Add a car", width=20, height=5)
button2.config(font=("Arial", 12, "bold"))
button2["command"] = button2.add
button2.place(x=430, y=50)
button3 = Sell(frame, text="Sell a car", width=20, height=5)
button3.config(font=("Arial", 12, "bold"))
button3["command"] = button3.sell
button3.place(x=50, y=200)
button4 = Change(frame, text="Change price", width=20, height=5)
button4.config(font=("Arial", 12, "bold"))
button4["command"] = button4.change
button4.place(x=430, y=200)
window.mainloop()
