num = int(input("\nEnter a number : "))

sum_of_digits = 0
while num > 0:
    digit = num % 10
    sum_of_digits += digit
    num //= 10

print(f"\nSum of digits : {sum_of_digits}")
