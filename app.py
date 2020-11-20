from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hi! This is just a test page made from Flask and Heroku."

if __name__=="__main__":
    app.run()