from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homesite.html')

@app.route('/home')
def home():
    return render_template('homesite.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/code')
def code():
    return render_template('code.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

if __name__ == '__main__':
    app.run(debug=True)