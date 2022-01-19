from flask import Flask, request
from dotenv import load_dotenv
import os
from utils.score import get_scores

app = Flask(__name__)
config = load_dotenv()

@app.route('/api', methods=['POST'])
def score():
    message = request.form.get('message')
    score = get_scores(message)
    return {
        'score': score
    }
if __name__ == "__main__":
    app.run(debug=os.environ.FLASK_DEBUG, port=os.environ.PORT)