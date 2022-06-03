import sys
import logging

# Rates to be applied to employees payment calculator
rates = {
    'MO': [
        # Rate for hour range
        # (from, to, rate)
        (0, 9, 25),
        (9, 18, 15),
        (18, 24, 20),
    ],
    'TU': [
        (0, 9, 25),
        (9, 18, 15),
        (18, 24, 20),
    ],
    'WE': [
        (0, 9, 25),
        (9, 18, 15),
        (18, 24, 20),
    ],
    'TH': [
        (0, 9, 25),
        (9, 18, 15),
        (18, 24, 20),
    ],
    'FR': [
        (0, 9, 25),
        (9, 18, 15),
        (18, 24, 20),
    ],
    'SA': [
        (0, 9, 30),
        (9, 18, 20),
        (18, 24, 25),
    ],
    'SU': [
        (0, 9, 30),
        (9, 18, 20),
        (18, 24, 25),
    ],
}


class RateNotDefined(Exception):
    """Exception to be called when the rate is not defined for a range"""
    
    def __init__(self, day, hour) -> None:
        super().__init__(f"No rate is defined for day: '{day}' and hour: '{hour}-{hour+1}'")


def get_rate(day: str, hour: int) -> int:
    """Get the rate corresponding to certain hour in a day.

    Args:
        day (str): Day of the week, in a 2 letters format. [MO-SU]
        hour (int): Hour of the day to evaluate

    Raises:
        RateNotDefined: If the hour-rate table does not include the rate for the 
                        specified day-hour, this error will be raised

    Returns:
        int: Rate for this specific day-hour combination to be paid.
    """
    for range_start, range_end, rate in rates[day.upper()]:
        if hour in range(range_start, range_end):
            return rate
    raise RateNotDefined(day, hour)


def rate_calculator(employee_data: str) -> str:
    """Function to calculate the total amount to be paid an employee 
    based on the hours they worked and the times during which they worked.

    Args:
        employee_data (str): input text to be processed.
        Example 1: RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00 
        Example 2: ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

    Returns:
        str: Total amount to be paid to the employee in the format: The amount to pay {EMPLOYEE} is: {AMOUNT} USD
    """
    pay_to = employee_data.split('=')[0]
    worked_hours = employee_data.split('=')[1]
    to_be_paid = 0
    for day_worked in worked_hours.split(','):
        day = day_worked[0:2]
        to_be_paid_for_this_day = 0
        for hour_worked in range(int(day_worked[2:4]), int(day_worked[8:10])):
            to_be_paid_for_this_day += get_rate(day, hour_worked)
        to_be_paid += to_be_paid_for_this_day
    return f'The amount to pay {pay_to} is: {to_be_paid} USD'


def process_file(txt_filename: str) -> None:
    """Process a .txt file to extract and calculate the exact amount to be paid
    to every employee in the file based on their worked hours

    Args:
        txt_filename (str): Filename of the desired .txt file to be processed
    """
    try:
        with open(txt_filename, 'r') as content:
            for line in content:
                print(rate_calculator(line))
    except FileNotFoundError:
        logging.error(f'File: {txt_filename} not found')

if __name__ == '__main__':
    # Check if filename is passed from command line as a positional argument.
    if len(sys.argv) > 1:
        process_file(sys.argv[1])
        exit()

    # If the filename is not in the arguments, ask for it
    print('Please input the .txt filename')
    print('txt file should be in the same folder of this script.')
    txt_filename = input("filename: ")
    process_file(txt_filename)
