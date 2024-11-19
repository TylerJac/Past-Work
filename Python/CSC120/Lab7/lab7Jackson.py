# ===============================================================

# Name: Tyler Jackson

# Date: 4/29/2024

# Course: CSC 120 NLE01

# Define the Employee class,
# Define the ProductionWorker class,
# Define the ShiftSupervisor class,
# Define the main function,
# Handle exceptions.

# References: in class

# ===============================================================

class Employee:
    """
    A class to represent an employee.

    Attributes:
    - name (str): The name of the employee.
    - number (str): The employee number.
    """

    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


class ProductionWorker(Employee):
    """
    A class to represent a production worker.

    Inherits from the Employee class.

    Attributes:
    - shift (int): The shift number (1 for day shift, 2 for night shift).
    - hourly_pay_rate (float): The hourly pay rate.
    """

    def __init__(self, name, number, shift=1, hourly_pay_rate=15.00):
        super().__init__(name, number)
        self.__shift = shift
        self.__hourly_pay_rate = hourly_pay_rate

    def set_shift(self, shift):
        self.__shift = shift

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift(self):
        return self.__shift

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate


class ShiftSupervisor(Employee):
    """
    A class to represent a shift supervisor.

    Inherits from the Employee class.

    Attributes:
    - shift (int): The shift number (1 for day shift, 2 for night shift).
    - annual_salary (float): The annual salary.
    - annual_production_bonus (float): The annual production bonus.
    """

    def __init__(self, name, number, shift=1, annual_salary=68000.0, annual_production_bonus=5000.0):
        super().__init__(name, number)
        self.__shift = shift
        self.__annual_salary = annual_salary
        self.__annual_production_bonus = annual_production_bonus

    def set_shift(self, shift):
        self.__shift = shift

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_production_bonus(self, annual_production_bonus):
        self.__annual_production_bonus = annual_production_bonus

    def get_shift(self):
        return self.__shift

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_production_bonus(self):
        return self.__annual_production_bonus


def main():
    """
    Main function to create objects of ProductionWorker and ShiftSupervisor classes,
    prompt the user to enter data, store the data in the objects, and display the information.
    """
    try:
        # Create ProductionWorker object
        name = input("Enter employee name: ")
        number = input("Enter employee number: ")
        shift = int(input("Enter shift number (1 for day shift, 2 for night shift): "))
        hourly_pay_rate = float(input("Enter hourly pay rate: "))
        worker = ProductionWorker(name, number, shift, hourly_pay_rate)

        # Create ShiftSupervisor object
        name = input("Enter supervisor name: ")
        number = input("Enter supervisor number: ")
        shift = int(input("Enter supervisor shift number: "))
        annual_salary = float(input("Enter supervisor annual salary: "))
        annual_production_bonus = float(input("Enter supervisor annual production bonus: "))
        supervisor = ShiftSupervisor(name, number, shift, annual_salary, annual_production_bonus)

        # Display information
        print("\nProduction Worker Information:")
        print("Name:", worker.get_name())
        print("Employee Number:", worker.get_number())
        print("Shift:", worker.get_shift())
        print("Hourly Pay Rate: ${:.2f}".format(worker.get_hourly_pay_rate()))

        print("\nShift Supervisor Information:")
        print("Name:", supervisor.get_name())
        print("Employee Number:", supervisor.get_number())
        print("Shift:", supervisor.get_shift())
        print("Annual Salary: ${:.2f}".format(supervisor.get_annual_salary()))
        print("Annual Production Bonus: ${:.2f}".format(supervisor.get_annual_production_bonus()))

    except ValueError:
        print("Error: Please enter valid numeric values for shift, hourly pay rate, salary, and bonus.")


if __name__ == "__main__":
    main()
