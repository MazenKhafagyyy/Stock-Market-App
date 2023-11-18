from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/company-data', methods=["POST"])
def receive_data():
    return render_template("result.html")

if __name__ == '__main__':
    app.run(debug=True)
