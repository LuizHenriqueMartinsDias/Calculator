class Calculator:
    def __init__(self):
        self.expression = ""

    def add(self,value:str):
        self.expression += value

    def change_signal(self):
        number = ""
        for index, digit in enumerate(self.expression[::-1]):
            if not (self.expression[-1:].isdigit()):
                self.expression = ""

            if digit.isdigit():
                number += digit
            else:
                signal = digit

                match signal:
                    case "+":
                        signal = "-"
                        self.expression = self.expression[:-(index + 1)]
                        self.expression += signal + number[::-1]
                    case "-":
                        signal = "+"
                        self.expression = self.expression[:-(index + 1)]
                        self.expression += signal + number[::-1]

                    case _:
                        signal = "+"
                        self.expression = self.expression[:-index]
                        self.expression += signal + number[::-1]

                return

    def power(self):
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

    def clear(self):
        self.expression = ""

    def delete(self):
        self.expression = self.expression[:-1]

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)

        except:
            self.expression = "0"
