# Try and Except Block
try:
    num1 = int(input("Enter Your First Numeber: "))
    num2 = int(input("Enter Your Second Numeber: "))
    result = num1/num2
    print(result)
except:
    print("Denominator can't be zero")