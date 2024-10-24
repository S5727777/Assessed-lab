def max_of_three(num1, num2, num3):
    """
    This function takes three integers as input and returns the maximum of the three given numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.

    Returns:
    mint: The maximum of the three numbers.
    """
    # Hint: you are required to make use of maximum variable that is returned by the function below.
    # Complete your code implementation here...
    if num3>=num2 and num1 <= num3:
        maximum = num3
    elif num2>=num1 and num3 <=num2:
        maximum = num2
    elif num1>=num2 and num3<=num1:
     maximum = num1
    else: print("syntax error")
    return maximum
# # You are out of the body function where you can test your code.
# Example usage:

maximum = max_of_three(86, 205, 356)
print(maximum, "is the maximum")
maximum = max_of_three(400, 86, 205)
print(maximum, "is the maximum")
maximum = max_of_three(86, 500, 356)
print(maximum, "is the maximum")

