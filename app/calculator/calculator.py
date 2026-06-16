from app.calculation.calculation import CalculationProgram

history = []

def main():
    print("Calculator V3 Project")

    while True:
        command = input(
            "\nEnter operation (+, -, *, /) or just choose help, history or exit: "
        ).strip().lower()
        if command == "exit":
            print("Goodbye and have a good day")
            return
        if command == "help":
            print("Command: ")
            print("+: Add: ")
            print("-: Subtract: ")
            print("*: Multiply: ")
            print("/: Divide: ")
            print("History")
            print("Exit")
            continue
        if command == "history":
            if not history:
                print("No calculation available to view")
            else:
                for item in history:
                    print(item)
            continue
        try:
            a = float(input("First Number: "))
            b = float(input("Second number: "))
            calc = CalculationProgram.create(command, a, b)
            result = calc.get_result()
            entry = f"{a} {command} {b} = {result}"
            history.append(entry)
            print("Result: ", result)
        except ValueError as e:
            print("Error:", e)
        except ZeroDivisionError as e:
            print("Error", e)
if __name__ == "__main__":
    main()

