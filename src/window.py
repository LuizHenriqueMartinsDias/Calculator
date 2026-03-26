from tkinter import *

class WindowInterface:
    display_value = ""
    def change_signal(self,display):
        if self.display_value == "Error":
            self.clear(display)
            return
        counter = 0
        for i in self.display_value:

            if not (i.isdigit()):
                number = self.display_value[-counter:]
                counter+=1
                self.display_value = self.display_value[:-counter]
                self.update_display(display)
                if i == "+":
                    self.display_value += str(int(number) * -1)
                else:
                    print(self.display_value)
                    self.display_value = self.display_value[-counter:]
                    print(self.display_value)
                    self.display_value += "+" + number

                break
            counter += 1
        self.update_display(display)
    def delete(self,display):
        if self.display_value == "Error":
            self.clear(display)
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
        counter = 0
        for n,i in enumerate(self.display_value):

            if n+1 == len(self.display_value):
                number = self.display_value
                self.display_value = self.display_value[:-counter]
                self.display_value += str(int(number) ** 2)
                break
            if not(i.isdigit()):
                number = self.display_value[-counter:]
                self.display_value = self.display_value[:-counter]
                self.display_value +=  str(int(number)**2)
                break
            counter += 1
        self.update_display(display)


    def button(self,label,display):
        if self.display_value == "Error":
            self.clear(display)
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
        display = Label(window,text=self.display_value ,height=6, justify="right")
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

        window.mainloop()

    def update_display(self,display):
        display.config(text=self.display_value)