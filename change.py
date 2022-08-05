from tkinter import *


class Change(Button):
    def change(self):
        class MyButton(Button):
            def action(self):
                art_nr = input1.get()
                price_new = input2.get()
                f = open(r'files\assortment.txt', 'r')
                car_list = f.readlines()
                f.close()
                changed = False
                for i in range(len(car_list)):
                    if car_list[i] == art_nr + "\n":
                        f = open(r'files\assortment.txt', 'w')
                        car_list[i + 4] = price_new + "\n"
                        for linie in car_list:
                            f.write(linie)
                        changed = True
                        break
                f.close()
                window.destroy()

                if changed:
                    window2 = Tk()
                    window2.geometry("300x100")
                    window2.title("Price changed!")
                    frame2 = Frame(window2, relief="ridge", borderwidth=5)
                    frame2.pack(fill="both", expand=1)
                    label_2 = Label(frame2, text="Price changed!")
                    label_2.pack(expand=1)
                    button2 = Button(frame2, text="OK", command=window2.destroy)
                    button2.pack(side="bottom", pady=5)
                    window2.mainloop()
                else:
                    window2 = Tk()
                    window2.geometry("300x100")
                    window2.title("Warning!")
                    frame2 = Frame(window2, relief="ridge", borderwidth=5)
                    frame2.pack(fill="both", expand=1)
                    label_2 = Label(frame2, text="Article number not found!")
                    label_2.pack(expand=1)
                    button2 = Button(frame2, text="OK", command=window2.destroy)
                    button2.pack(side="bottom", pady=5)
                    window2.mainloop()

        window = Tk()
        window.geometry("500x400")
        window.title("Change price")
        frame = Frame(window, relief="ridge", borderwidth=5)
        frame.pack(fill="both", expand=1)
        label = Label(frame, text="Enter the new price:")
        label.config(font=("Arial", 14, "bold"))
        label.place(x=80, y=30)
        label1 = Label(frame, text="Article number:")
        label1.place(x=100, y=100)
        input1 = Entry(frame, bd=2, width=22)
        input1.place(x=200, y=100)
        label2 = Label(frame, text="New price:")
        label2.place(x=100, y=140)
        input2 = Entry(frame, bd=2, width=22)
        input2.place(x=200, y=140)
        button = MyButton(frame, text="Set price")
        button["command"] = button.action
        button.place(x=180, y=220)
        window.mainloop()
