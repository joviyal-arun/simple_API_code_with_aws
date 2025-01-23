from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle button click
@app.route("/button-click")
def button_click():
    return "<h1>Button clicked! Hello Arunachalam Here is your static content.</h1>"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
