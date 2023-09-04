num = int(input("Sum of numbers until: "))

sum = 0

for i in range(num):
    sum += i+1

print(f"Sum of from 1 until {num} =", sum)