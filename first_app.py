from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!! This is my first flask web app"

app.run(host='0.0.0.0', port=5000)