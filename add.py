# add.py

from tkinter import *


class Add(Button):
    def add(self):
        class MyButton(Button):
            def action1(self):
                f = open(r'files\assortment.txt', 'a')
                content = input1.get()
                f.write(content + "\n")
                content = input2.get()
                f.write(content + "\n")
                content = input3.get()
                f.write(content + "\n")
                content = input4.get()
                f.write(content + "\n")
                content = input5.get()
                f.write(content + "\n")
                f.write("\n")
                f.close()
                window.destroy()
        window = Tk()
        window.geometry("550x400")
        window.title("Add a car")
        frame = Frame(window, relief="ridge", borderwidth=5)
        frame.pack(fill="both", expand=1)
        label_main = Label(frame, text="Enter the information about the new car:")
        label_main.config(font=("Arial", 14, "bold"))
        label_main.place(x=50, y=10)
        label1 = Label(frame, text="Article number:")
        label1.place(x=100, y=100)
        input1 = Entry(frame, bd=2, width=22)
        input1.place(x=200, y=100)
        label2 = Label(frame, text="Brand:")
        label2.place(x=100, y=140)
        input2 = Entry(frame, bd=2, width=22)
        input2.place(x=200, y=140)
        label3 = Label(frame, text="Model:")
        label3.place(x=100, y=180)
        input3 = Entry(frame, bd=2, width=22)
        input3.place(x=200, y=180)
        label4 = Label(frame, text="Year of construction:")
        label4.place(x=100, y=220)
        input4 = Entry(frame, bd=2, width=22)
        input4.place(x=200, y=220)
        label5 = Label(frame, text="Price:")
        label5.place(x=100, y=260)
        input5 = Entry(frame, bd=2, width=22)
        input5.place(x=200, y=260)
        button = MyButton(frame, text="Add Car")
        button["command"] = button.action1
        button.place(x=180, y=320)
        window.mainloop()
