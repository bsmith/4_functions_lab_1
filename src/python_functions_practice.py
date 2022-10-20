import datetime

def return_10():
    return 10

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    number_1 = int(string_1)
    number_2 = int(string_2)
    return number_1 + number_2

# FULL_MONTH_NAMES = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
def number_to_full_month_name(number):
    dt = datetime.datetime(2022, number, 1)
    return dt.strftime("%B")
    # return FULL_MONTH_NAMES[number - 1]
    # if number == 1:
    #     return "January"
    # elif number == 3:
    #     return "March"
    # elif number == 9:
    #     return "September"

def number_to_short_month_name(number):
    return number_to_full_month_name(number)[:3]
    # if number == 1:
    #     return "Jan"
    # elif number == 4:
    #     return "Apr"
    # elif number == 10:
    #     return "Oct"

def volume_of_a_cube(side_length):
    return side_length**3

def reverse_string(string):
    string_reversed = ''
    for index in range(len(string)):
        string_reversed += string[-(index + 1)]
    return string_reversed
    # return string[::-1]

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) / 1.8, 4)
