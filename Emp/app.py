import traceback
import datetime
import logging

from Emp.employee import EmailAlreadyExistsException
from Emp.Developer import Developer
from Emp.Recruiter import Recruiter


def main():
    mike = Recruiter(name='Mike', salary=123, email='asdfgh@gnail.com')
    nike = Developer(name='Nike', salary=245, email='sfdXSfsgd@gnail.com', tech_stack=['python', 'java', 'css'])
    dike = Developer(name='Dike', salary=342, email='sdf123sdf@gnail.com', tech_stack=['css', 'js', 'c#', 'ruby'])

    print(mike.work())
    print(nike.work())
    print(dike.work())
    print(mike, nike, dike, sep=', ')
    print(mike.check_salary(), nike.check_salary(), dike.check_salary(), sep='\n')
    print(nike > mike, mike != dike, dike < nike)
    print(nike.__dict__)
    print(dike.__dict__)
    print(nike.check_stack(), dike.check_stack(), sep=' when ')


if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException:
        with open('logs.txt', 'a') as txt_file:
            message = f"{datetime.date.today()} {datetime.datetime.now().hour}:{datetime.datetime.now().minute} {traceback.format_exc()}"
            logging.basicConfig(filename='logs.txt', encoding='utf-8', level=logging.DEBUG)
            logging.debug(message)
