class Employee:
    def __init__(self, id=None, name='', position='', salary=0.0, hire_date=''):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date
    def __str__(self):
        return f"Employee(id={self.id}, name='{self.name}', position='{self.position}', salary={self.salary}, hire_date='{self.hire_date}')"
