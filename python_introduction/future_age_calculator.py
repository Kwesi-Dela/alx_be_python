user_age = input("How old are you? ")
user_age = int(user_age)     # Convert input to integer because input is a text string
future_age = user_age + 27  # Calculate age in 2050 years because 2023 is the assumed current year
print(f"In 2050 you will be {future_age} years old.")  # Output the result