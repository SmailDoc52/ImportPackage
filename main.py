import datetime

from art import tprint
from application import salary
from application.db import people
from application.salary import calculate_salary

if __name__ == '__main__':
    now = datetime.datetime.now()
    print(now.strftime("%d.%m.%Y"))
    salary.calculate_salary()
    print(now.strftime("%d.%m.%Y"))
    people.get_employees()
    tprint("Project_modules")

