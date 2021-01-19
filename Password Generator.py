# this is a password generator

import random


def main():
    string_list = ""

    symbols = "!@#$%&!@#$%&!@#$%&!@#$%&"
    numbers = "12345678901234567890"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    number_of_passwords = int(input("How many passwords would you like to generate? "))
    print()
    length_of_passwords = int(input("How long do you want your passwords to be? "))
    print()

    lower_case_status = input("Would you like to include lower case letters (Y/N)? ")
    if lower_case_status == "Y" or lower_case_status == "y" or lower_case_status == "yes" or lower_case_status == "YES":
        string_list += lower_case
    print()

    upper_case_status = input("Would you like to include upper case letters (Y/N)? ")
    if upper_case_status == "Y" or upper_case_status == "y" or upper_case_status == "yes" or upper_case_status == "YES":
        string_list += upper_case
    print()

    numbers_status = input("Would you like to include numbers (Y/N)? ")
    if numbers_status == "Y" or numbers_status == "y" or numbers_status == "yes" or numbers_status == "YES":
        string_list += numbers
    print()

    symbols_status = input("Would you like to include symbols (Y/N)? ")
    if symbols_status == "Y" or symbols_status == "y" or symbols_status == "yes" or symbols_status == "YES":
        string_list += symbols
    print()

    generator(string_list, number_of_passwords, length_of_passwords)

    print()
    print("-------Program Terminated-------")


def generator(string_list, number_of_passwords, length_of_passwords):
    password = ""

    print("Passwords: ")
    print()
    for j in range(0, number_of_passwords):
        password = ""
        for i in range(0, length_of_passwords):
            character = string_list[random.randint(0, len(string_list)) - 1]
            password += character
        print(password)


main()
