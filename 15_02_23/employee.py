import datetime
from datetime import date,timedelta

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return 'I come to the office'

    def __gt__(self, other):
        if self.salary > other.salary:
            return f'{self.name} is a lucky guy!'
        else:
            return f'{self.name} is a looser!'

    def check_salary(self):
        now = datetime.datetime.now()
        fromdate = date(now.year, now.month, 1)
        todate = date(now.year, now.month, now.day)
        daygenerator = (fromdate + timedelta(x) for x in range((todate - fromdate).days + 1))
        working_days = sum(1 for day in daygenerator if day.weekday() < 5)
        return f'{self.name} has {self.salary * working_days} $ per {working_days} days of this month'


class Recruiter(Employee):

    def work(self, motyvation):
        return f'"{super().work()} and start {motyvation}" - say {self.name}'

    def __str__(self):
        return f'{self.name}: {__class__.__name__}'


class Developer(Employee):
    def work(self, motyvation):
        return f'"{super().work()} and start {motyvation}" - say {self.name}'

    def __str__(self):
        return f'{self.name}: {__class__.__name__}'

    def __new__(cls, name, salary, tech_stack):
        tech_stack = super().__new__(cls)
        tech_stack.name = name
        return tech_stack

    def __init__(self, name, salary, tech_stack):
        self.name = name
        self.tech_stack = tech_stack
        self.salary = salary

    def check_stack(self):
        return f'{self.name} works with {len(self.tech_stack)} technologies'


if __name__ == '__main__':
    mike, nike, dike = Recruiter('Mike', 123), Developer('Nike', 245, ['python', 'java', 'css']), Developer('Dike', 342,
                                                                                                            ['css',
                                                                                                             'js', 'c#',
                                                                                                             'ruby'])
    print(mike.work('hiring'))
    print(nike.work('coding'))
    print(dike.work('coding'))
    print(mike, nike, dike, sep=', ')
    print(mike.check_salary(), nike.check_salary(), dike.check_salary(), sep='\n')
    print(nike > mike, mike > dike, dike > nike)

    print(nike.__dict__)
    print(dike.__dict__)
    print(nike.check_stack(), dike.check_stack(), sep=' when ')
