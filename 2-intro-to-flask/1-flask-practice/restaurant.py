from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'

@app.route('/about')
def about():
    return 'A family owned restaurant!'

@app.route('/team')
def team():
    return 'Built by two best friends!'

if __name__ == "__main__":
    app.run()
