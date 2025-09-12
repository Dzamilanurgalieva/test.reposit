def average1(numbers):
    total_sum = sum(numbers)
    count = len(numbers)
    average = total_sum / count
    return average


def main():
    numbers = []
    while True:
        number_str = input()
        if not number_str.strip():
            break
        try:
            number = float(number_str)
            numbers.append(number)
        except ValueError:
            print("ОШИБКА")

    if numbers:
        avg = average1(numbers)
        print(f"Среднее значение:{avg}")
    else:
        print("ОШИБКА")

main()
