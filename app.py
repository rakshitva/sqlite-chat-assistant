from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route to render the frontend (HTML page)
@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML page when the user accesses the root URL

# Route to handle the chat query
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    query = data.get("query")
    
    # Handle the query (you can add your own logic here for the chatbot)
    response = handle_query(query)
    
    return jsonify({"response": response})

# Function to handle user queries (modify this with your own logic)
def handle_query(query):
    # Example logic: if the query matches a certain text, return a predefined response
    if query.lower() == "who is the manager of the sales department?":
        return "John Doe is the manager of the Sales department."
    elif query.lower() == "what is the company mission?":
        return "Our mission is to innovate and provide excellent customer service."
    # Add more logic or AI model calls to handle different queries
    return "Sorry, I couldn't understand the query."

if __name__ == "__main__":
    # Running the app
    app.run(debug=True, host="0.0.0.0", port=5000)
