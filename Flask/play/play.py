from flask import Flask, render_template
app = Flask(__name__)

# Level 1
@app.route('/play')
def play():
    return render_template("index.html", times=3, color="blue")


# Level 2
@app.route('/play/<x>')
def play_times(x):
    return render_template("index.html", times=int(x), color="blue")


# Level 3
@app.route('/play/<x>/<color>')
def play_color(x, color):
    return render_template("index.html", times=int(x), color=color)


if __name__ == "__main__":
    app.run(debug=True)