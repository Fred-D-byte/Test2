# Global list to store employee data
employees = []

# Global counter
employee_count = 0

def add_employee():
    """Add a new employee to the system."""
    global employee_count

    name = input("Enter Employee Name: ")
    ssn = input("Enter Employee SSN (e.g., 123121234): ")
    phone = input("Enter Employee Phone (e.g., (111)222-3333): ")
    email = input("Enter Employee Email: ")
    salary = input("Enter Employee Salary: ")

    employee = f"{name}, {ssn}, {phone}, {email}, {salary}"
    employees.append(employee)
    employee_count += 1
    print("\nEmployee added successfully!\n")

def view_employees():
    """Display all employees in the system."""
    if not employees:
        print("\nNo employees in the system.\n")
    else:
        print("\n--- Employee List ---")
        for idx, emp in enumerate(employees, 1):
            print(f"{idx}. {emp}")
        print("----------------------\n")

def main():
    print("Welcome to the Employee Management System")

    while True:
        print(f"\nThere are ({employee_count}) employees in the system.")
        print("Select an option:")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

# Run the program
main()
