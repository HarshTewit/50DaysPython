def calculate_minutes(age_in_years):
    DAYS_IN_YEAR = 365.25
    HOURS_IN_DAY = 24 
    MINUTES_IN_HOUR = 60

    total_days = age_in_years * DAYS_IN_YEAR
    total_hours = total_days * 24 
    total_minutes = total_hours * 60

    return round(total_days), round(total_hours), round(total_minutes)

while True:
    try:
        age = float(input("Enter you age in years."))
        days, hours, minutes = calculate_minutes(age)

        print("\n You are approx: ")
        print(f" - {days} days old. \n - {hours} hours old. \n - {minutes} minutes old.")
        again = input("Would you like to try again? (y/n)").strip().lower()

        if(again != 'y'):
            print("Goodbye!")
            break
    except:
        print("Enter a valid value for age please.")
