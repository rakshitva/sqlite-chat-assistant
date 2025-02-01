from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Mock function to simulate bot answers based on queries
def get_answer(query):
    if "employee names" in query.lower():
        return "Alice, Bob, Charlie, David"
    elif "departments" in query.lower():
        return "HR, IT, Sales, Marketing"
    else:
        return "Sorry, I couldn't understand your query. Could you please rephrase it?"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    try:
        user_query = request.json.get('query')
        if not user_query:
            return jsonify({'error': 'No query provided'}), 400

        response = get_answer(user_query)
        return jsonify({'answer': response}), 200

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your request'}), 500

if __name__ == '__main__':
    app.run(debug=True)

