import sqlite3
from employee import Employee

class EmployeeDAO:
    def __init__(self, dbname = "employeedb.sqlite"):
        self.conn = sqlite3.connect(dbname)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS employee(
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT,
                              position TEXT,
                              salary REAL,
                              hire_date TEXT)
                              ''')
            
    def insert(self, employee : Employee):
        with self.conn:
            x = self.conn.execute("INSERT INTO employee(name, position, salary, hire_date) VALUES(?, ?, ?, ?)", (employee.name, employee.position, employee.salary, employee.hire_date))
        employee.id = x.lastrowid
        return employee.id 
    
    def get_byid(self, id):
        with self.conn:
            x = self.conn.execute(
                "SELECT * FROM employee WHERE id = ?", (id,)
            )
        row = x.fetchone()
        return Employee(*row) if row else None

    def get_all(self):
        with self.conn:
            x = self.conn.execute(
                "SELECT * FROM employee"
            )
        rows = x.fetchall()
        z = []
        for row in rows:
            z.append(Employee(*row))
        for i in z:
            print(str(i))
        return z

    def update(self, employee: Employee):
        with self.conn:
            self.conn.execute(
                "UPDATE employee SET name = ?, position = ?, salary = ?, hire_date = ? WHERE id = ?",
                (employee.name, employee.position, employee.salary, employee.hire_date, employee.id)
            )

    def delete(self, emp_id: int):
        with self.conn:
            self.conn.execute("DELETE FROM employee WHERE id = ?", (emp_id,))

    
    

