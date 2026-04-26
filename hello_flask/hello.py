from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/Champion')
def champion():
    return "Champion!"


@app.route('/say/<name>')
def say(name):
    return "Hi " + name


@app.route('/repeat/<int:num>/<word>')
def repeat(num, word):
    return word * num


# @app.route('/not_found/error')
# def not_found():
    # return "Sorry! No response. Try again."
    
@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)