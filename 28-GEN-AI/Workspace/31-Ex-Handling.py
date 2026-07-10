try:
    a = int(input("Enter first Number:"))
    b = int(input("Enter second Number:"))

    result = a / b

    print("Result : ", result)

except Exception as ve:
    print("Please enter only numbers : ", ve)
except ValueError as e:
    print("Exception Occured : ", e)

print("Program Execution Completed")