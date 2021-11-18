from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')
    # return "<p>Hello, World!</p>"


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/details")
def details():
    return render_template('details.html')


@app.route("/portfolio")
def portfolio():
    return render_template('portfolio.html')


@app.route("/projects")
def projects():
    return render_template('projects.html')


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
    # app.run(debug=True)   Default
