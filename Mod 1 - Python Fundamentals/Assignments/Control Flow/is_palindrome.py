num = int(input("\nEnter a number : "))

temp = num
rev = 0
while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10

if(temp == rev):
    print(f"\n{temp} is a palindrome.")
else:
    print(f"\n{temp} is not a palindrome.")