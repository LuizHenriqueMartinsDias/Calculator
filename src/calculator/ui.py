from tkinter import *

from src.calculator.logic import Calculator


class CalculatorUI:
    """
        Graphical user interface for the calculator using Tkinter.

        Handles user interactions and updates the display.
        """
    def __init__(self):
        self.calc = Calculator()

    def keyboard_event(self, display, event) -> None:
        """
        Handles keyboard input events.

        Args:
            display (Label): The display widget.
            event (Event): The keyboard event.
        """
        #Matches the key pressed
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

    def button(self, label, display) -> None:
        """
        Handles button click events.

        Args:
            label (str): The button label/value.
            display (Label): The display widget.
        """

        #Matches the button pressed and calls the dedicated method
        match label:
            case "C":
                self.calc.clear()

            case "x²":
                self.calc.power()

            case "+/-":
                self.calc.change_signal()

            case "=":
                self.calc.calculate()

            case "<":
                self.calc.delete()

            case _:
                self.calc.add(label)

        self.update_display(display)

    def create_window(self):
        """
        Creates and configures the main application window.
        """
        #Window Configuration
        window = Tk()
        window.title("Calculator")
        window.geometry("300x450")
        window.config(background="gray")

        #Configure grid layout (responsive resizing)
        for i in range(6):  # linhas (0 a 5)
            window.rowconfigure(i, weight=1)

        for i in range(4):  # colunas (0 a 4)
            window.columnconfigure(i, weight=1)

        #Display Container
        fixed_frame = Frame(window, width=200, height=100, bg="white")
        fixed_frame.grid(row=0, column=0, columnspan=4, sticky="nsew")

        #Prevent frame from resizing to fit content
        fixed_frame.grid_propagate(False)
        fixed_frame.rowconfigure(0, weight=1)
        fixed_frame.columnconfigure(0, weight=1)

        # Display label (aligned to the right)
        display = Label(
            fixed_frame,
            text=self.calc.expression,
            font=("Segoe UI", 20, "bold"),
            anchor="e",  # alinha à direita corretamente
            fg="black",
            bg="#A9A9A9",
            padx=10
        )


        display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button definitions: (label, function, row, column)
        bttns = [
            ("7", lambda: self.button("7", display), 2, 0),
            ("8", lambda: self.button("8", display), 2, 1),
            ("9", lambda: self.button("9", display), 2, 2),
            ("x", lambda: self.button("*", display), 2, 3),

            ("4", lambda: self.button("4", display), 3, 0),
            ("5", lambda: self.button("5", display), 3, 1),
            ("6", lambda: self.button("6", display), 3, 2),
            ("-", lambda: self.button("-", display), 3, 3),

            ("1", lambda: self.button("1", display), 4, 0),
            ("2", lambda: self.button("2", display), 4, 1),
            ("3", lambda: self.button("3", display), 4, 2),
            ("+", lambda: self.button("+", display), 4, 3),

            ("+/-", lambda: self.button("+/-", display), 5, 0),
            ("0", lambda: self.button("0", display), 5, 1),
            (".", lambda: self.button(".", display), 5, 2),
            ("=", lambda: self.button("=", display), 5, 3),

            ("x²", lambda: self.button("x²", display), 1, 0),
            ("C", lambda: self.button("C", display), 1, 1),
            ("<", lambda: self.button("<", display), 1, 2),
            ("/", lambda: self.button("/", display), 1, 3)
        ]
        #Create Button dynamically
        for label, function, row, col in bttns:
            Button(
                window,
                text=label,
                command=function,
                bd=0,
                relief="flat",
                activeforeground="white",
                font=("Segoe UI", 14),
                bg="#2d2f33",
                fg="white",
                activebackground="#3a3d42",
            ).grid(row=row, column=col, padx=1, pady=1, sticky="nsew")

        #Keyboard Binding
        binds = ["=", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "/", "+", "-", "."]
        for bind_value in binds:
            window.bind(bind_value, func=lambda x: self.keyboard_event(display, x))
        window.bind("<BackSpace>", func=lambda x: self.keyboard_event(display, x))
        window.mainloop()

    def update_display(self, display):
        """
          Updates the calculator display.

          Args:
              display (Label): The display widget.
          """
        display.config(text=self.calc.expression)
