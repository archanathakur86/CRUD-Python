from flask import Flask, request

app = Flask(__name__)

employees = [{
        "id": 1,
        "name": "Kritika",
        "age": 17,
        "email": "kritika@gmail.com",
        "role": "Web Developer",
        "department": "IT"
    }]
next_id = 2

@app.post("/employees")
def create_employee():
    global next_id

    data = request.get_json()

    employee = {
        "id": next_id,
        "name": data["name"],
        "age": data["age"],
        "email": data["email"],
        "role": data["role"],
        "department": data["department"]
    }

    employees.append(employee)
    next_id += 1

    return employee, 201

@app.get("/employees")
def get_employees():
    return employees

@app.get("/employees/<int:id>")
def get_employee(id):

    for employee in employees:
        if employee["id"] == id:
            return employee

    return {"message": "Employee not found"}, 404

@app.get("/employees/<int:id>")
def get_employee(id):

    for employee in employees:
        if employee["id"] == id:
            return employee

    return {"message": "Employee not found"}, 404

@app.delete("/employees/<int:id>")
def delete_employee(id):

    for employee in employees:

        if employee["id"] == id:
            employees.remove(employee)

            return { "message": "Employee deleted"}

    return {"message": "Employee not found"}, 404