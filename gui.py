import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QLabel, QListWidget, QLineEdit
)
from employee import Employee
from employee_dao import EmployeeDAO

class EmployeeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Employee Manager")
        self.setGeometry(100, 100, 400, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel("Employee Records")
        self.layout.addWidget(self.label)

        self.load_button = QPushButton("Load Employees")
        self.layout.addWidget(self.load_button)

        self.employee_list = QListWidget()
        self.layout.addWidget(self.employee_list)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        self.layout.addWidget(self.name_input)

        self.position_input = QLineEdit()
        self.position_input.setPlaceholderText("Position")
        self.layout.addWidget(self.position_input)

        self.salary_input = QLineEdit()
        self.salary_input.setPlaceholderText("Salary")
        self.layout.addWidget(self.salary_input)

        self.hire_date_input = QLineEdit()
        self.hire_date_input.setPlaceholderText("Hire Date (YYYY-MM-DD)")
        self.layout.addWidget(self.hire_date_input)

        self.save_button = QPushButton("Save New Employee")
        self.layout.addWidget(self.save_button)

        self.update_button = QPushButton("Update Employee")
        self.layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Delete Employee")
        self.layout.addWidget(self.delete_button)

        self.dao = EmployeeDAO("employee_db.sqlite3")

        self.load_button.clicked.connect(self.load_employees)
        self.save_button.clicked.connect(self.save_employee)
        self.update_button.clicked.connect(self.update_employee)
        self.delete_button.clicked.connect(self.delete_employee)

    def load_employees(self):
        self.employee_list.clear()
        employees = self.dao.get_all()
        for emp in employees:
            display_text = f"{emp.id} - {emp.name} - {emp.position} - ${emp.salary}"
            self.employee_list.addItem(display_text)

        if employees:
            self.employee_list.setCurrentRow(0)
            self.show_employee_details(employees[0])

    def show_employee_details(self, employee):
        self.name_input.setText(employee.name)
        self.position_input.setText(employee.position)
        self.salary_input.setText(str(employee.salary))
        self.hire_date_input.setText(employee.hire_date)

    def save_employee(self):
        name = self.name_input.text()
        position = self.position_input.text()
        salary_text = self.salary_input.text()
        hire_date = self.hire_date_input.text()

        try:
            salary = float(salary_text)
        except ValueError:
            self.label.setText("Invalid salary input.")
            return

        new_emp = Employee(None, name, position, salary, hire_date)
        self.dao.insert(new_emp)

        self.label.setText("Employee added!")
        self.load_employees()

        self.name_input.clear()
        self.position_input.clear()
        self.salary_input.clear()
        self.hire_date_input.clear()

    def update_employee(self):
        selected_item = self.employee_list.currentItem()

        if not selected_item:
            self.label.setText("Please select an employee to update.")
            return

        employee_id = int(selected_item.text().split(' - ')[0])
        employee = self.dao.get_byid(employee_id)

        employee.name = self.name_input.text()
        employee.position = self.position_input.text()
        employee.salary = float(self.salary_input.text())
        employee.hire_date = self.hire_date_input.text()

        self.dao.update(employee)
        
        self.label.setText("Employee updated!")
        self.load_employees()

    def delete_employee(self):
        selected_item = self.employee_list.currentItem()

        if not selected_item:
            self.label.setText("Please select an employee to delete.")
            return

        employee_id = int(selected_item.text().split(' - ')[0])
        self.dao.delete(employee_id)

        self.label.setText("Employee deleted!")
        self.load_employees()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeApp()
    window.show()
    sys.exit(app.exec())
