def calculator():
    user_input = input()

    parts = user_input.split()

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("ОШИБКА - Деление на ноль!")
            return
        else:
            result = num1 / num2
    else:
        print("ОШИБКА")
        return

    print(f"{result}")


calculator()
