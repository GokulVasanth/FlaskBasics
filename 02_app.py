from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('02_index.html')


@app.route('/signup_form')
def signup_form():
    return render_template('02_signup.html')


@app.route('/thankyou')
def thankyou():
    username = request.args.get('username')
    return render_template('02_thankyou.html', username = username)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('02_404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
