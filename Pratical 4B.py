# Try and Multiple Except Block
try:
    number = [3, 4, 5, 6]
    print(number[5])
except ZeroDivisionError:
    print("Denominator can't be zero")
except:
    print("Index Out of Bound")