numbers = []

for i in range(3):
    n = int(input(f"Enter integer {i + 1}: "))
    numbers.append(n)

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print(f"Maximum Number:", maximum)