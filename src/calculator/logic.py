class Calculator:
    """
    Handles the core logic of the calculator.

    Manages the current expression and performs mathematical operations.
    """

    def __init__(self):
        self.expression = ""

    def add(self,value:str) -> None:
        """
        adds an element to the expression,

        Args:
            value (str): the digit or sign to add
        """

        #If the last element of the expression is not a digit replace it with the given value
        if not(value.isdigit()) and not(self.expression[-1:].isdigit()):
            self.expression = self.expression[:-1]
            self.expression += value
            return

        #adds the value to the expression
        self.expression += value

    def change_signal(self):
        """
        Changes the sign of the last number in the expression

        Example:
            +5 -> -5
            -5 -> +5
        """


        number = ""
        #loop to get the last number of the expression
        for index, digit in enumerate(self.expression[::-1]):

            if digit.isdigit():
                number += digit
            else:
                sign = digit

                #matches the sign of the number
                match sign:
                    case "+":
                        sign = "-"
                        self.expression = self.expression[:-(index + 1)]
                        self.expression += sign + number[::-1]
                    case "-":
                        sign = "+"
                        self.expression = self.expression[:-(index + 1)]
                        self.expression += sign + number[::-1]

                    case _:
                        sign = "+"
                        self.expression = self.expression[:-index]
                        self.expression += sign + number[::-1]

                return

    def power(self) -> None:
        """
        Squares the last number in the expression.
        """
        number = ""
        for index, digit in enumerate(self.expression[::-1]):
            if not (self.expression[-1:].isdigit()):
                self.expression = ""
                return
            if digit.isdigit():
                number += digit
            else:
                number = number[::-1]
                self.expression = self.expression[:-index]
                self.expression += str(int(number) ** 2)

                return
            if index + 1 == len(self.expression):
                number = number[::-1]
                self.expression = ""
                self.expression += str(int(number) ** 2)
                return

    def clear(self) ->None:
        """
        clears the expression.
        """
        self.expression = ""

    def delete(self) ->None:
        """
        deletes the last element in the expression.
        """
        self.expression = self.expression[:-1]

    def calculate(self):
        """
        Evaluates the expression.
        """

        try:
            result = eval(self.expression)
            self.expression = str(result)

        except:
            self.expression = "0"
