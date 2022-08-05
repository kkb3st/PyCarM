from tkinter import *


class Sell(Button):
    def sell(self):
        class MyButton(Button):
            def action(self):
                art_nr = input1.get()
                f = open(r'files\assortment.txt', 'r')
                car_list = f.readlines()
                f.close()
                deleted = False
                for i in range(len(car_list)):
                    if car_list[i] == art_nr + "\n":
                        f = open(r'files\assortment.txt', 'w')
                        car_list = car_list[:i] + car_list[i + 6:]
                        for line in car_list:
                            f.write(line)
                        deleted = True
                        break
                f.close()
                window.destroy()
                if deleted:
                    window2 = Tk()
                    window2.geometry("300x100")
                    window2.title("Car sold!")
                    frame2 = Frame(window2, relief="ridge", borderwidth=5)
                    frame2.pack(fill="both", expand=1)
                    label2 = Label(frame2, text="Car removed!")
                    label2.pack(expand=1)
                    button2 = Button(frame2, text="OK", command=window2.destroy)
                    button2.pack(side="bottom", pady=5)
                    window2.mainloop()
                else:
                    window2 = Tk()
                    window2.geometry("300x100")
                    window2.title("Warning!")
                    frame2 = Frame(window2, relief="ridge", borderwidth=5)
                    frame2.pack(fill="both", expand=1)
                    label2 = Label(frame2, text="Article number not found!")
                    label2.pack(expand=1)
                    button2 = Button(frame2, text="OK", command=window2.destroy)
                    button2.pack(side="bottom", pady=5)
                    window2.mainloop()
        window = Tk()
        window.geometry("500x400")
        window.title("Sell car")
        frame = Frame(window, relief="ridge", borderwidth=5)
        frame.pack(fill="both", expand=1)
        label = Label(frame, text="Which car do you want to sell?")
        label.config(font=("Arial", 14, "bold"))
        label.place(x=50, y=10)
        label1 = Label(frame, text="Article number:")
        label1.place(x=100, y=100)
        input1 = Entry(frame, bd=2, width=22)
        input1.place(x=200, y=100)
        button = MyButton(frame, text="Sell")
        button["command"] = button.action
        button.place(x=180, y=220)
        window.mainloop()
