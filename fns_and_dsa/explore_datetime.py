from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    # Print in "YYYY-MM-DD HH:MM:SS" format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=days_to_add)
    # Print in "YYYY-MM-DD" format
    print("Future date:", future_date.strftime("%Y-%m-%d"))


display_current_datetime()
calculate_future_date()

