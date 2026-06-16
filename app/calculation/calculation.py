from app.operations.add import add
from app.operations.subtract import subtract
from app.operations.multiply import multiply
from app.operations.divide import divide

class Calculation:
    def __init__(self, operation, a, b):
        self.operation = operation
        self.a = a
        self.b = b
    def get_result(self):
        operation = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
        }
        if self.operation not in operation:
            raise ValueError("Invalid operation")
        return operation[self.operation](self.a, self.b)

class CalculationProgram:
    @staticmethod
    def create(operation, a, b):
        return Calculation(operation, a, b)
    
