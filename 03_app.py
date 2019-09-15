from flask import Flask, render_template, request
from pyfiles.app03.function import Word

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('03_index.html')

@app.route('/output')
def output():
    word = request.args.get('word')
    letter = Word()
    output = letter.validate(letter.check(word))
    return render_template('03_output.html', output = output)

if __name__ == '__main__':
    app.run(debug=True)