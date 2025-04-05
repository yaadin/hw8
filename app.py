import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Employee Manager")
        self.setFixedSize(600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.title_label = QLabel("Employee Management System")
        self.layout.addWidget(self.title_label)

        self.add_button = QPushButton("Add Employee")
        self.view_button = QPushButton("View All Employees")
        self.update_button = QPushButton("Update Employee")
        self.delete_button = QPushButton("Delete Employee")

        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.view_button)
        self.layout.addWidget(self.update_button)
        self.layout.addWidget(self.delete_button)

        self.employee_list = QListWidget()
        self.layout.addWidget(self.employee_list)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())