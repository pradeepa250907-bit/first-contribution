from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to the Open Source Workshop!</h1><p>Visit /hello to get greeted.</p>"

@app.route('/hello')
def hello():
    # INTENTIONAL BUG, fix it 
    # 'greeting' is misspelled below as 'greetng' to throw a NameError
    greeting = "You did it!" 
    return f"<h1>{greeting}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
