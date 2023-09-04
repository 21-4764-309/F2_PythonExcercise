import NumberConverter

decimal_value = int(input("Enter a decimal number: "))

binary_result = NumberConverter.decToBinary(decimal_value)
print(f"Binary: {binary_result}")

binary_input = "101010"
hexadecimal_result = NumberConverter.binaryToN(binary_input, "hex")
print(f"Hexadecimal: {hexadecimal_result}")

octal_result = NumberConverter.decToOctal(decimal_value)
print(f"Octal: {octal_result}")

hexadecimal_result = NumberConverter.decToHex(decimal_value)
print(f"Hexadecimal: {hexadecimal_result}")

#Nexus-Code89 is my github community account i was late to notice the mistake