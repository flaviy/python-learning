def division(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("Second argument must not be zero")
    except TypeError:
        print("Arguments must be numbers")
    else:
        print(result)



