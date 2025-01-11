def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero Division Error"

print(divide(1,0))