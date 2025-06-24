def safe_divide(numerator, denumerator):
    try:
        result = float(numerator) / float(denumerator)
        return print(f"The result of the division is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")



# try:
#   # Code that might raise an exception
# except ExceptionType:
#   # Code to handle the exception
# else:
#   # Code that executes if no exception occurs
# finally:
#   # Code that always executes, regardless of exceptions
