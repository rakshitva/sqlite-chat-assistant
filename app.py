from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('chat_assistant.db')
    conn.row_factory = sqlite3.Row
    return conn

# Function to fetch manager by department
def fetch_manager_by_department(department):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT manager FROM employees WHERE department = ?", (department,))
    manager = cursor.fetchone()
    conn.close()
    return manager

# Function to fetch employees by department
def fetch_employees_by_department(department):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM employees WHERE department = ?", (department,))
    employees = cursor.fetchall()
    conn.close()
    return [employee['name'] for employee in employees]

@app.route('/chat', methods=['POST'])
def chat():
    query = request.json['query'].lower()  # Convert query to lowercase for case-insensitivity
    
    # Handling different queries
    if "manager of the" in query:
        department = query.split("manager of the")[1].strip()
        manager = fetch_manager_by_department(department)
        if manager:
            return jsonify({"response": f"The manager of the {department} department is {manager['manager']}."})
        else:
            return jsonify({"response": f"No manager found for the department '{department}'."})
    
    if "employees in the" in query:
        department = query.split("employees in the")[1].strip()
        employees = fetch_employees_by_department(department)
        if employees:
            return jsonify({"response": f"Employees in the {department} department: " + ", ".join(employees)})
        else:
            return jsonify({"response": f"No employees found in the department '{department}'."})
    
    return jsonify({"response": "Sorry, I didn't understand your query. Please ask about department managers or employees."})

if __name__ == '__main__':
    app.run(debug=True)
