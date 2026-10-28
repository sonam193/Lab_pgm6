
from employee import employee_details

def test_employee_details():
    result = employee_details("Sonam", "EMP101", "IT", "50000")

    expected = "Name: Sonam\nEmployee ID: EMP101\nDepartment: IT\nSalary: 50000"

    assert result == expected
