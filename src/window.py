from tkinter import *

class WindowInterface:
    display_value = ""
    def change_signal(self,display):
        if self.display_value == "Error":
            self.clear(display)
            return
        number = ""
        for index, digit in enumerate(self.display_value[::-1]):
            if not (self.display_value[-1:].isdigit()):
                self.display_value = "Error"
                self.update_display(display)
                return
            if digit.isdigit():
                number += digit
            else:
                signal = digit
                print(signal)
                match signal:
                    case "+":
                        signal = "-"
                        self.display_value = self.display_value[:-(index + 1)]
                        self.display_value += signal + number[::-1]
                        self.update_display(display)
                    case "-":
                        signal = "+"
                        self.display_value = self.display_value[:-(index + 1)]
                        self.display_value += signal + number[::-1]
                        self.update_display(display)
                    case _:
                        signal = "+"
                        self.display_value = self.display_value[:-index]
                        self.display_value += signal + number[::-1]
                        self.update_display(display)
                return

    def delete(self,display,event=None):
        if self.display_value == "Error":
            self.clear(display)
            return
        if event:
            self.display_value = self.display_value[:-1]
            self.update_display(display)
            return
        self.display_value = self.display_value[:-1]
        self.update_display(display)


    def calculate(self,display):
        if self.display_value == "Error":
            self.clear(display)
            return

        if self.display_value[-1:].isdigit():
            self.display_value = str(eval(self.display_value))
            self.update_display(display)
        else:
            self.display_value = "Error"
            self.update_display(display)


    def power(self,display):
        if self.display_value == "Error":
            self.clear(display)
            return
        number = ""
        for index, digit in enumerate(self.display_value[::-1]):
            if not(self.display_value[-1:].isdigit()):
                self.display_value = "Error"
                self.update_display(display)
                return
            if digit.isdigit():
                number += digit
            else:
                number = number[::-1]

                self.display_value = self.display_value[:-index]
                self.display_value += str(int(number) ** 2)
                self.update_display(display)
                return
            if index + 1 == len(self.display_value):
                number = number[::-1]
                self.display_value = ""
                self.display_value += str(int(number) ** 2)
                self.update_display(display)
                return


    def button(self,label,display,event=None):
        if self.display_value == "Error":
            self.clear(display)
            return
        if event:
            self.display_value += event.char
            self.update_display(display)
            return
        self.display_value += label
        self.update_display(display)


    def clear(self,display):
        self.display_value = ""
        self.update_display(display)


    def create_window(self):

        #Window Config
        window = Tk()
        window.title("Calculator")
        window.geometry("320x450")
        window.config(background="gray")


        #Display
        display = Label(window,text=self.display_value ,height=6, justify="right",background="#A9A9A9",)
        display.grid(row=0, column=0, columnspan=10, sticky="nsew")

        #Buttons
        Button(window,text="1",command=lambda label="1":self.button(label,display),width=10,height=4).grid(row=4, column=1)
        Button(window,text="2",command=lambda label="2":self.button(label,display),width=10,height=4).grid(row=4, column=2)
        Button(window,text="3",command=lambda label="3":self.button(label,display),width=10,height=4).grid(row=4, column=3)
        Button(window,text="4",command=lambda label="4":self.button(label,display),width=10,height=4).grid(row=3, column=1)
        Button(window,text="5",command=lambda label="5":self.button(label,display),width=10,height=4).grid(row=3, column=2)
        Button(window,text="6",command=lambda label="6":self.button(label,display),width=10,height=4).grid(row=3, column=3)
        Button(window,text="7",command=lambda label="7":self.button(label,display),width=10,height=4).grid(row=2, column=1)
        Button(window,text="8",command=lambda label="8":self.button(label,display),width=10,height=4).grid(row=2, column=2)
        Button(window,text="9",command=lambda label="9":self.button(label,display),width=10,height=4).grid(row=2, column=3)
        Button(window,text="0",command=lambda label="0":self.button(label,display),width=10,height=4).grid(row=5, column=2)
        Button(window,text="+",command=lambda label="+":self.button(label,display),width=10,height=4).grid(row=4, column=4)
        Button(window,text="-",command=lambda label="-":self.button(label,display),width=10,height=4).grid(row=3, column=4)
        Button(window,text="x",command=lambda label="*":self.button(label,display),width=10,height=4).grid(row=2, column=4)
        Button(window,text="+/-",command=lambda display=display:self.change_signal(display),width=10,height=4).grid(row=5, column=1)
        Button(window,text="=",command=lambda display=display:self.calculate(display),width=10,height=4).grid(row=5, column=4)
        Button(window,text=".",command=lambda label=".":self.button(label,display),width=10,height=4).grid(row=5, column=3)
        Button(window,text="C",command=lambda display=display:self.clear(display),width=10,height=4).grid(row=1, column=2)
        Button(window,text="<",command=lambda display=display:self.delete(display),width=10,height=4).grid(row=1, column=3)
        Button(window,text="/",command=lambda label="/":self.button(label,display),width=10,height=4).grid(row=1, column=4)
        Button(window,text="x²",command=lambda display=display:self.power(display),width=10,height=4).grid(row=1, column=1)
        binds = ["0","1","2","3","4","5","6","7","8","9","*","/","+","-","."]
        for bind_value in binds:
             window.bind(bind_value,func=lambda label=bind_value:self.button(label=label,event=label,display=display))
        window.bind("<BackSpace>", func=lambda label="<BackSpace>": self.delete(event=label, display=display))
        window.mainloop()

    def update_display(self,display):
        display.config(text=self.display_value)