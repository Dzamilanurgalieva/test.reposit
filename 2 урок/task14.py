def count1(numbers):
    count = 0
    index = 0

    while index < len(numbers):
        if numbers[index] > 10:
            count += 1
        index += 1

    return count


numbers = list(map(int, input().split()))
result = count1(numbers)
print(result)