from Emp.employee import Employee


class Developer(Employee):
    def __init__(self, name, salary, email, tech_stack):
        super().__init__(name, salary, email)
        self.tech_stack = tech_stack

    def work(self):
        return f'{super().work()[:-1]} and start coding.'

    def check_stack(self):
        return f'{self.name} works with {len(self.tech_stack)} technologies'
