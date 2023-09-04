number = int(input("Enter number: "))

count = 0
smallest = number % 10
highest = number % 10

while number > 0:
    digit = number % 10

    if digit < smallest:
        smallest = digit

    if digit > highest:
        highest = digit

    count += 1
    number = number // 10

print(f"Number of digits:", count)
print(f"Smallest:", smallest)
print(f"Highest:", highest)


