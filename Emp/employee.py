import datetime
import csv

from datetime import date, timedelta


class EmailAlreadyExistsException(Exception):
    pass


class Employee:
    def __init__(self, name, salary, email):
        self.name = name
        self.salary = salary
        self.email = email
        self.validate()
        self.save_email()

    def save_email(self):
        with open('emails.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['name', 'email'])
            writer.writeheader()
            writer.writerow({"name": self.name, "email": self.email})
        #  csv_file.write(self.email.lower().split() + '\n')

    def validate(self):
        with open('emails.csv') as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=['name', 'email'])
            if self.email.strip() in (x['email'] for x in reader):
                raise EmailAlreadyExistsException

    def work(self):
        return 'I come to the office.'

    def __str__(self):
        return f'{self.name}: {self.__class__.__name__}'

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def check_salary(self):
        now = datetime.datetime.now()
        fromdate = date(now.year, now.month, 1)
        todate = date(now.year, now.month, now.day)
        daygenerator = (fromdate + timedelta(x) for x in range((todate - fromdate).days + 1))
        working_days = sum(1 for day in daygenerator if day.weekday() < 5)
        return f'{self.name} has {self.salary * working_days} $ per {working_days} days of this month'
