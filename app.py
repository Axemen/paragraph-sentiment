from flask import Flask, render_template, request, redirect
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

analyzer = SentimentIntensityAnalyzer()


@app.route('/', methods = ['GET', 'POST'])
def home():
    score = 0

    if request.method == "POST":
        paragraph = request.form['paragraph']
        print(paragraph)

        score = analyzer.polarity_scores(paragraph)['compound']





    return render_template('index.html', score = score)

if __name__ == '__main__':
    app.run(debug = True)
