from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from utils.score import get_scores

app = Flask(__name__)

@app.errorhandler(404)
def invalid(error):
    return render_template('404.html')

@app.route('/api', methods=['POST'])
def score():
    message = request.form.get('message')
    score = get_scores(message)
    return {
        'score': score
    }
if __name__ == "__main__":
    app.run()