from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_date

print("Current Date and Time:", display_current_datetime())

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = datetime.now() + timedelta(days=number_of_days)
    return future_date.strftime("%Y %B %d")

print("Future Date:", calculate_future_date())