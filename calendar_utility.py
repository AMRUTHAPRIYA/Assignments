# Task 4: Date and Calendar Utility
# Uses Python's built-in 'calendar' and 'datetime' modules.

import calendar
import datetime

def display_calendar_utility():
    print("--- Date and Calendar Utility ---")
    
    try:
        # Ask the user for a year and month
        year = int(input("Enter year (e.g., 2026): "))
        month = int(input("Enter month (1-12): "))
        
        # Simple validation for the month range
        if not (1 <= month <= 12):
            print("Invalid month! Please enter a number between 1 and 12.")
            return

        print(f"\nCalendar for {calendar.month_name[month]} {year}:\n")
        
        # Print the formatted calendar grid for that specific month
        cal_str = calendar.month(year, month)
        print(cal_str)
        
        # Get today's actual date
        today = datetime.date.today()
        
        # Check if today matches the year and month the user entered
        if today.year == year and today.month == month:
            print(f"--> Today is {today.strftime('%B %d, %Y')} (This falls within the displayed month!)")
        else:
            print(f"--> Today is {today.strftime('%B %d, %Y')} (This is outside the displayed month).")
            
    except ValueError:
        print("Invalid input! Please make sure to enter valid numbers for the year and month.")

if __name__ == "__main__":
    display_calendar_utility()
    