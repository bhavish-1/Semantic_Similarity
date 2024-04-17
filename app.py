from flask import Flask, render_template, request
from main import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_similarity', methods=['POST'])
def calculate_similarity():
    if request.method == 'POST':
        text1 = request.form['text1']
        text2 = request.form['text2']

        similarity_score = main(text1, text2)
        return render_template('index.html', similarity_score=similarity_score)

if __name__ == '__main__':
    app.run(debug=True)
