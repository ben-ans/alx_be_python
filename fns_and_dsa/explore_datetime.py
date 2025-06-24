from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%d-%m-%y %H:%M:%S")
    print("The current time and date: ", current_date)

# display_current_datetime()

def calculate_future_timedate():
    day = int(input("enter the number of days: "))
    future_date = datetime.now() + timedelta(days=day)
    future_date = future_date.strftime("%d-%m-%y %H:%M:%S")
    print("The future datetime will be: ", future_date)

# calculate_future_timedate()


def main():
    display_current_datetime()
    calculate_future_timedate()
if __name__ == "__main__":
    main()