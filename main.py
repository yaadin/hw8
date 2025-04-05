from employee import Employee
from employee_dao import EmployeeDAO

def main():
    dao = EmployeeDAO()
    new_emp = Employee(name="Rakhatbekov Meder", position="Boss", salary=70000, hire_date="2025-05-01")
    
    # INSER
    emp_id = dao.insert(new_emp)
    print(f"Inserted employee with ID: {emp_id}")

    #GET BY ID
    emp = dao.get_byid(emp_id)
    print("Retrieved by ID:", emp)

    #GET ALL
    print("\nAll employees:")
    dao.get_all()

    #UPDATE
    emp.salary = 75000 
    dao.update(emp)
    print("\nAfter update:", dao.get_byid(emp_id))

    #DELETE
    dao.delete(emp_id)
    print("\nAfter deletion:", dao.get_byid(emp_id))

if __name__ == "__main__":
    main()