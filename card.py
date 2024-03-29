#!env/bin/python3
"""
Python script to check validity of credit card numbers
Author : Zoalktoom
"""

import sys, os, time, datetime


def usage():
    msg = """
        
        usage:
        python3 card.py card_number
        
        example:
        python3 card.py 34678253793
        
    """
    print(msg)


def get_cc_number():
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    return sys.argv[1]


def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum


def validate(cc_num):
    # reverse the credit card number
    cc_num = cc_num[::-1]
    # convert to integer list
    cc_num = [int(x) for x in cc_num]
    # double every second digit
    doubled_second_digit_list = list()
    digits = list(enumerate(cc_num, start=1))
    for index, digit in digits:
        if index % 2 == 0:
            doubled_second_digit_list.append(digit * 2)
        else:
            doubled_second_digit_list.append(digit)

    # add the digits if any number is more than 9
    doubled_second_digit_list = [sum_digits(x) for x in doubled_second_digit_list]
    # sum all digits
    sum_of_digits = sum(doubled_second_digit_list)
    # return True or False
    return sum_of_digits % 10 == 0

if __name__ == "__main__":
    print ('Please wait...\n')
    time.sleep(7)
    print(validate(get_cc_number()))
    print('\n')
    time.sleep(2)
