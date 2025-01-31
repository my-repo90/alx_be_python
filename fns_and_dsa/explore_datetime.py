from datetime import timedelta , datetime

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:",current_date.strftime("%x %X"))


def calculate_future_date():
    
    number_days = int(input("Enter the number of days to add to the current date: "))
    current_date = datetime.now()
    future_date = current_date + timedelta(number_days)
    print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))


def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()