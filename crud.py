employees=[{
    "id":1,
    "name":"Kritika",
    "age":17,
    "email":"Kritika@gmail.com",
    "role":"Web-developer",
    "department":"IT"
}]
next_id=2

def create_employee():
    global next_id
    print("\n -----------CREATE EMPLOYEE-----------")
    employee={
        "id":next_id,
        "name":input("Enter name:"),
        "age":int(input("Enter age:")),
        "email":input("Enter email:"),
        "role":input("Enter role:"),
        "department":input("Enter department:")
    }
    employees.append(employee)
    print("\n Created successfully")

    print("Employee id:",next_id)
    next_id+=1

def read_employees():
    print("\n -----------READ EMPLOYEES-----------")
    for employee in employees:
        print("ID:",employee["id"])
        print("Name:",employee["name"])
        print("Age:",employee["age"])
        print("Email:",employee["email"])
        print("Role:",employee["role"])
        print("Department:",employee["department"])

    if len(employees)==0:
        print("\n No employees found")

def update_employee():
    print("\n----------- UPDATE EMPLOYEE -----------")

    employee_id = int(input("Enter employee id: "))

    for employee in employees:
        if employee["id"] == employee_id:

            print("\nEnter new details:")
            name = input(f"Name ({employee['name']}): ")
            age = input(f"Age ({employee['age']}): ")
            email = input(f"Email ({employee['email']}): ")
            role = input(f"Role ({employee['role']}): ")
            department = input(f"Department ({employee['department']}): ")

            if name != "":
                employee["name"] = name

            if age != "":
                employee["age"] = int(age)

            if email != "":
                employee["email"] = email

            if role != "":
                employee["role"] = role

            if department != "":
                employee["department"] = department

            print("\nUpdated successfully")
            break

    else:
        print("\nEmployee not found")

def delete_employee():
    print("\n----------- DELETE EMPLOYEE -----------")

    employee_id = int(input("Enter employee id: "))

    for i in range (len(employees)):
        if employees[i]["id"] == employee_id:
            confirm = input("Are you sure you want to delete? (yes/no): ")

            if confirm == "yes":
                employees.remove(employees[i])
                print("\nDeleted successfully")
            else:
                print("\nEmployee was not deleted")

            break
    else:
        print("\nEmployee not found")

while True:
    print("\n -----------EMPLOYEE MANAGEMENT-----------")
    print("1. Create employee")
    print("2. Read employees")
    print("3. Update employee")
    print("4. Delete employee")
    print("5. Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        create_employee()
    elif choice==2:
        read_employees()
    elif choice==3:
        update_employee()
    elif choice==4:
        delete_employee()
    elif choice==5:
        break
    else:
        print("\n Invalid choice")
    


