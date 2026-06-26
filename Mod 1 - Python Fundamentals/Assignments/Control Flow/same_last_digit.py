def getlastDigit(num):
    return num % 10

def sameLastDigit(a, b):
    return getlastDigit(a) == getlastDigit(b)

if __name__ == "__main__":
    a = int(input("\nEnter the first number: "))
    b = int(input("Enter the second number: "))
    
    if sameLastDigit(a, b):
        print("\nTrue.")
    else:
        print("\nFalse.")
