from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = ['Gokul Vasanth','subash','varun']
    return render_template('basic.html',name=name)

@app.route('/info/<name>')
def firstmethod(name):
    return ("This is my {} page ".format(name))

if __name__ == '__main__':
    app.run(debug=True)