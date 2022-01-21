from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from utils.score import get_scores
from errors.invalid import InvalidAPIUsage
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = Flask(__name__)
config = load_dotenv()

@app.errorhandler(404)
def invalid(error):
    return render_template('404.html')

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(message="Method Not Allowed"), 405

@app.errorhandler(InvalidAPIUsage)
def invalid_usage(error):
    return jsonify(error.to_dict()), 400

@app.route('/api', methods=['POST'])
def score():
    message = request.form.get('message')
    if message is None or message == '':
        raise InvalidAPIUsage("No message provided!")
    score = get_scores(message)
    return {
        'score': score
    }
if __name__ == "__main__":
    app.run(port=os.environ.PORT)