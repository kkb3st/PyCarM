# show.py

from tkinter import *


class Show(Button):
    def show(self):
        window = Tk()
        window.geometry("500x400")
        window.title("Show Cars")
        frame = Frame(window, relief="ridge", borderwidth=5)
        frame.pack(fill="both", expand=1)
        label = Label(frame, text="List of all Cars:")
        label.config(font=("Arial", 14, "bold"))
        label.pack(pady=20)
        frame2 = Frame(frame, relief="ridge", borderwidth=1)
        frame2.pack(pady=20, padx=30)
        f = open(r"files\assortment.txt", "r")
        content = f.readlines()
        scrollbar = Scrollbar(frame2)
        car_list = Listbox(frame2, yscrollcommand=scrollbar.set, width=50)
        i = 0
        output = ""
        for line in content:
            if i == 0:
                output = "Article number: " + line
                i += 1
            elif i == 1:
                output = "Brand: " + line
                i += 1
            elif i == 2:
                output = "Model: " + line
                i += 1
            elif i == 3:
                output = "Year of construction: " + line
                i += 1
            elif i == 4:
                output = "Price: " + line
                i += 1
            elif i == 5:
                output = ""
                i = 0
            car_list.insert(END, output)
        f.close()
        scrollbar.config(command=car_list.yview)
        car_list.pack(side="left", fill="both")
        scrollbar.pack(side="left", fill="y")
        button = Button(frame, text="OK", command=window.destroy, width=10, height=2)
        button.config(font=("Arial", 10))
        button.pack(pady=10)
        window.mainloop()
