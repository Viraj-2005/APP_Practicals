# Try Except and Else Block
try:
    num1 = int(input("Enter Your Number: "))
    assert num1 % 2 == 0
except:
    print("Not an Even Number")
else:
    reciprocal = 1/num1
    print("Reciprocal of given number", reciprocal)

