def calculate_age_number(prompt):
    """
    Asks user for age and add 10 years to the age number based on the given age.

    Returns:
    int: The calculated age number.
    """
    value = int(input(prompt))
    while value < 5:
        print("Please enter an age above 5")
        value = int(input(prompt))
    return value + 10

age = calculate_age_number("\nWhat is your age? ")
print(f"Your age in 10 years will be: {age}")