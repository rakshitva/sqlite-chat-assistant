from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize SQLite database
DATABASE = 'chat_assistant.db'

# Function to execute queries
def execute_query(query, params=()):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

# Function to fetch query results
def fetch_query(query, params=()):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.close()
    return result

# Route for the root of the website
@app.route("/")
def home():
    return "Welcome to the Chat Assistant API!"

# Route to handle chat queries
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    query = data.get('query', '')
    
    if not query:
        return jsonify({"response": "No query provided."}), 400

    # Look for the query in the database
    if 'manager' in query.lower():
        department = query.split('manager of the ')[1].split(' department')[0]
        result = fetch_query("SELECT manager FROM department WHERE name=?", (department,))
        if result:
            response = f"The manager of the {department} department is {result[0][0]}."
        else:
            response = f"No manager found for the department '{department}'."
    else:
        response = "I'm sorry, I don't understand the question."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
