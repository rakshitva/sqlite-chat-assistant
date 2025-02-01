from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock function to simulate bot answers based on queries
def get_answer(query):
    # Handle specific queries
    if "employee names" in query.lower():
        return "Alice, Bob, Charlie, David"  # Mocked response
    elif "departments" in query.lower():
        return "HR, IT, Sales, Marketing"  # Mocked response
    else:
        return "Sorry, I couldn't understand your query. Could you please rephrase it?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        # Get the user query from the frontend
        user_query = request.json.get('query')
        if not user_query:
            return jsonify({'error': 'No query provided'}), 400

        # Process the query and get the response from the bot
        response = get_answer(user_query)

        # Return the response back to the frontend
        return jsonify({'answer': response}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your request'}), 500

if __name__ == '__main__':
    app.run(debug=True)

