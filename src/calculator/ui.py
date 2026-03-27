from tkinter import *

from src.calculator.logic import Calculator


class CalculatorUI:
    def __init__(self):
        self.calc = Calculator()
    def keyboard_event(self,display,event):
        match event.char:
            case "\b":
                self.calc.delete()
                self.update_display(display)
            case "=":
                self.calc.calculate()
                self.update_display(display)
            case _:
                self.calc.add(event.char)
                self.update_display(display)


    def button(self,label,display,event=None):

        match label:
            case "C":
                self.calc.clear()
                self.update_display(display)
            case "x²":
                self.calc.power()
                self.update_display(display)
            case "+/-":
                self.calc.change_signal()
                self.update_display(display)
            case "=":
                self.calc.calculate()
                self.update_display(display)
            case "<":
                self.calc.delete()
                self.update_display(display)
            case _:
                self.calc.add(label)
                self.update_display(display)


    def create_window(self):

        #Window Config
        window = Tk()
        window.title("Calculator")
        window.geometry("260x450")
        window.config(background="gray")
        window.resizable(False,False)

        #Display
        display = Label(window,text=self.calc.expression,font=("Segoe UI",14) ,height=4,fg="white", justify="right",background="#A9A9A9",)
        display.grid(row=0, column=0, columnspan=10, sticky="nsew")

        #Buttons
        BTN_BG = "#2d2f33"
        BTN_FG = "white"
        BTN_ACTIVE = "#3a3d42"
        FONT = ("Segoe UI", 14)
        bttns = [
            ("7", lambda: self.button("7", display), 2, 1),
            ("8", lambda: self.button("8", display), 2, 2),
            ("9", lambda: self.button("9", display), 2, 3),
            ("x", lambda: self.button("*", display), 2, 4),

            ("4", lambda: self.button("4", display), 3, 1),
            ("5", lambda: self.button("5", display), 3, 2),
            ("6", lambda: self.button("6", display), 3, 3),
            ("-", lambda: self.button("-", display), 3, 4),

            ("1", lambda: self.button("1", display), 4, 1),
            ("2", lambda: self.button("2", display), 4, 2),
            ("3", lambda: self.button("3", display), 4, 3),
            ("+", lambda: self.button("+", display), 4, 4),

            ("+/-", lambda: self.button("+/-", display), 5, 1),
            ("0", lambda: self.button("0", display), 5, 2),
            (".", lambda: self.button(".", display), 5, 3),
            ("=", lambda: self.button("=", display), 5, 4),

            ("x²", lambda: self.button("x²", display), 1, 1),
            ("C", lambda: self.button("C", display), 1, 2),
            ("<", lambda: self.button("<", display), 1, 3),
            ("/", lambda: self.button("/", display), 1, 4)
        ]
        for label, function, row, col in bttns:
            Button(
                window,
                text=label,
                command=function,
                width=5,
                height=2,
                bd=0,
                relief="flat",
                activeforeground="white",
                font=FONT,
                bg=BTN_BG,
                fg=BTN_FG,
                activebackground=BTN_ACTIVE,
            ).grid(row=row, column=col ,padx=2, pady=2, sticky="nsew")

        binds = ["=","0","1","2","3","4","5","6","7","8","9","*","/","+","-","."]
        for bind_value in binds:
             window.bind(bind_value,func=lambda x:self.keyboard_event(display,x))
        window.bind("<BackSpace>", func=lambda x:self.keyboard_event(display,x))
        window.mainloop()

    def update_display(self,display):
        display.config(text=self.calc.expression)