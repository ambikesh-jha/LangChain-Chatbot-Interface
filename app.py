from flask import Flask, request, jsonify, render_template
from model import get_model
from templates import get_prompt_template
from langchain import LLMChain

app = Flask(__name__)

# Initialize the model and prompt template
llm = get_model()
prompt = get_prompt_template()
llm_chain = LLMChain(llm=llm, prompt=prompt)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Chatbot API endpoint
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    question = data.get("question", "")
    if not question:
        return jsonify({"error": "Question is required"}), 400

    # Get the response from the model
    response = llm_chain.invoke(question)
    
    # Convert the response to a string if it is not already
    if isinstance(response, dict):
        # Extract text if response is a dictionary (adapt this as needed)
        response_text = response.get("text", "No text found.")
    else:
        response_text = str(response)
    
    return jsonify({"answer": response_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
