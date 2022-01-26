from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os

from mongoengine import ValidationError
from utils.score import get_scores
from errors.invalid import InvalidAPIUsage
from db.data import connectDB, createDoc
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

app = Flask(__name__)
load_dotenv()
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
    data = request.get_json()
    message = data['message']
    if message is None or message == '':
        raise InvalidAPIUsage("No message provided!")
    score = get_scores(message)
    return {
        'score': score
    }

@app.route('/update', methods=['POST'])
def update():
    data = request.get_json()
    message = data['message']
    label = data['label']
    try:
        db = connectDB()
        res = jsonify(str(createDoc(message, label)))
        db.close()
        return res
    except ValidationError as e:
        raise InvalidAPIUsage(str(e))

if __name__ == "__main__":
    app.run(port=os.environ.get('PORT'))