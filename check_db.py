import sqlite3

# Connect to the database
conn = sqlite3.connect("chat_assistant.db")
cursor = conn.cursor()

# Query data from Employees table
cursor.execute("SELECT * FROM Employees")
employees = cursor.fetchall()
print("Employees:")
for row in employees:
    print(row)

# Query data from Departments table
cursor.execute("SELECT * FROM Departments")
departments = cursor.fetchall()
print("\nDepartments:")
for row in departments:
    print(row)

# Close connection
conn.close()
