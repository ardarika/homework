from Emp.employee import Employee


class Recruiter(Employee):
    def work(self):
        return f'{super().work()[:-1]} and start hiring.'
