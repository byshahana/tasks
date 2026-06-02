def safe_divide(a,b):
    if b==0:
       raise ZeroDivisionError("Cannot divide by zero")
    return a/b
print (safe_divide(6,3))