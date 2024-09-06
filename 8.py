import jdatetime
import datetime


def show_gregorian(birth):
    thisyear = datetime.datetime.now().year
    age = thisyear - birth
    return age


def show_jalali_age(birth):
    thisyear = jdatetime.datetime.now().year
    age = thisyear - birth
    return age


# print("You are", show_jalali_age(int(input("Enter your birth year : "))))
print("You are", show_gregorian(int(input("Enter your birth year : "))))
