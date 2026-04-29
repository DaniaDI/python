from flask import Flask ,redirect,url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "hello <h1>HELLO</h1>"
    


@app.route("/user/<name>")
def user(name):
    return f"hello {name}"


@app.route("/admin")
def admin():
    return redirect(url_for("user",name="dania"))




if __name__ ==("__main__"):
    app.run()

 