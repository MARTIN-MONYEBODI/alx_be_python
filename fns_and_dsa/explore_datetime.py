import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date

print("Current Date and Time:", display_current_datetime())

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = display_current_datetime() + datetime.timedelta(days=number_of_days)
    return future_date

print("Future Date:", calculate_future_date())