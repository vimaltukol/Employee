import pytest 
from Employee import get_employee_info
def test_get_employee_info():
    #sample data
    name="Alice Smith"
    emp_id="E202"
    department = "HR"
    salary = 60000
    expected_output = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary:.2f}"
    )
    assert get_employee_info(name, emp_id, department, salary) == expected_output