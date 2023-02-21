import datetime
from datetime import date, timedelta


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

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


class Recruiter(Employee):
    def work(self):
        return f'"{super().work()[:-1]} and start hiring." - say {self.name}'


class Developer(Employee):
    def __init__(self, name, salary, tech_stack):
        super().__init__(name, salary)
        self.tech_stack = tech_stack

    def work(self):
        return f'"{super().work()[:-1]} and start coding." - say {self.name}'

    def check_stack(self):
        return f'{self.name} works with {len(self.tech_stack)} technologies'


if __name__ == '__main__':
    mike, nike, dike = Recruiter('Mike', 123), Developer('Nike', 245, ['python', 'java', 'css']), \
                       Developer('Dike', 342, ['css', 'js', 'c#', 'ruby'])
    print(mike.work())
    print(nike.work())
    print(dike.work())
    print(mike, nike, dike, sep=', ')
    print(mike.check_salary(), nike.check_salary(), dike.check_salary(), sep='\n')
    print(nike > mike, mike != dike, dike < nike)

    print(nike.__dict__)
    print(dike.__dict__)
    print(nike.check_stack(), dike.check_stack(), sep=' when ')
