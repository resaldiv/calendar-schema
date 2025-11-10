#!/usr/bin/env python3
"""
Simple Calendar Utilities Script

This script provides basic calendar functionality including:
- Display current month calendar
- Find day of the week for a given date
- Calculate days between two dates
"""

import calendar
from datetime import datetime, date


def display_current_month():
    """Display the current month's calendar."""
    now = datetime.now()
    print(f"\n--- {calendar.month_name[now.month]} {now.year} ---")
    print(calendar.month(now.year, now.month))


def get_day_of_week(year, month, day):
    """Get the day of the week for a given date."""
    try:
        target_date = date(year, month, day)
        day_name = calendar.day_name[target_date.weekday()]
        return f"{target_date.strftime('%Y-%m-%d')} is a {day_name}"
    except ValueError as e:
        return f"Invalid date: {e}"


def days_between_dates(date1, date2):
    """Calculate the number of days between two dates."""
    try:
        d1 = datetime.strptime(date1, '%Y-%m-%d').date()
        d2 = datetime.strptime(date2, '%Y-%m-%d').date()
        difference = abs((d2 - d1).days)
        return f"There are {difference} days between {date1} and {date2}"
    except ValueError as e:
        return f"Invalid date format: {e}"


def is_leap_year(year):
    """Check if a given year is a leap year."""
    return calendar.isleap(year)


def main():
    """Main function to demonstrate calendar utilities."""
    print("=== Calendar Utilities ===")
    
    # Display current month
    display_current_month()
    
    # Get current date info
    today = date.today()
    print(f"\nToday is: {today}")
    print(get_day_of_week(today.year, today.month, today.day))
    
    # Check if current year is leap year
    current_year = today.year
    if is_leap_year(current_year):
        print(f"{current_year} is a leap year!")
    else:
        print(f"{current_year} is not a leap year.")
    
    # Example: Days between today and New Year
    new_year = f"{current_year + 1}-01-01"
    print(f"\n{days_between_dates(str(today), new_year)}")
    
    # Display next month
    if today.month == 12:
        next_month_year = today.year + 1
        next_month = 1
    else:
        next_month_year = today.year
        next_month = today.month + 1
    
    print(f"\n--- Next Month: {calendar.month_name[next_month]} {next_month_year} ---")
    print(calendar.month(next_month_year, next_month))


if __name__ == "__main__":
    main()