# employee_system.py
from abc import ABC, abstractmethod
from typing import List

class Employee(ABC):
    def __init__(self, name: str, employee_id: int, job_title: str):
        self.name = name
        self.employee_id = employee_id
        self.job_title = job_title

    @abstractmethod
    def calculate_salary(self) -> float:
        """Return the salary for this employee."""
        raise NotImplementedError

    def __str__(self):
        return f"{self.employee_id:04d} | {self.name:20s} | {self.job_title:15s} | {self.calculate_salary():8.2f}"

class Worker(Employee):
    def __init__(self, name: str, employee_id: int, hourly_rate: float, hours_worked: float):
        super().__init__(name, employee_id, "Worker")
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self) -> float:
        # Basic calculation: hourly_rate * hours_worked
        return self.hourly_rate * self.hours_worked

class Manager(Employee):
    def __init__(self, name: str, employee_id: int, fixed_salary: float, bonus: float = 0.0):
        super().__init__(name, employee_id, "Manager")
        self.fixed_salary = fixed_salary
        self.bonus = bonus

    def calculate_salary(self) -> float:
        return self.fixed_salary + self.bonus

class EmployeeSystem:
    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, emp: Employee):
        self.employees.append(emp)

    def total_payroll(self) -> float:
        return sum(e.calculate_salary() for e in self.employees)

    def display_all(self):
        print("ID   | Name                 | Job Title       | Salary")
        print("-----+----------------------+-----------------+---------")
        for e in self.employees:
            print(e)
        print("-----+----------------------+-----------------+---------")
        print(f"Total payroll: {self.total_payroll():.2f}")

# --- Demo / Test ---
if __name__ == "__main__":
    sys = EmployeeSystem()

    # create several employees (workers and managers)
    sys.add_employee(Worker("Alice Johnson", 1, hourly_rate=15.0, hours_worked=160))
    sys.add_employee(Worker("Bob Karimov", 2, hourly_rate=12.5, hours_worked=120))
    sys.add_employee(Manager("Clara Smith", 3, fixed_salary=3000.0, bonus=500.0))
    sys.add_employee(Manager("Dmitry Ivanov", 4, fixed_salary=2500.0, bonus=250.0))

    # display
    sys.display_all()

    # simple checks (tests)
    assert abs(sys.employees[0].calculate_salary() - (15.0*160)) < 1e-6
    assert abs(sys.employees[2].calculate_salary() - (3000.0+500.0)) < 1e-6
    print("\nAll sample salary checks passed.")
