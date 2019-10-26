from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')


@app.route("/fitness")
def fitness():
    return render_template('fitness.html')


@app.route("/earnings")
def earnings():
    return render_template('earnings.html')


if __name__ == "__main__":
    app.run(port=5000)