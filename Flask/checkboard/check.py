from flask import Flask , render_template , url_for

app = Flask(__name__)

@app.route("/")
def check():
  return render_template(
    "index.html",
    row=8,
    col=8,
    color1="white",
    color2="black"
)

@app.route("/<int:x>")
def checkrow(x):
    return render_template(
        "index.html",
        row=x,
        col=8,
        color1="white",
        color2="black"
)
@app.route("/<int:x>/<int:y>")
def checkboard(x,y):
    return render_template(
        "index.html",
        row=x,
        col=y,
        color1="white",
        color2="black"
)

@app.route("/<int:x>/<int:y>/<color>")
def checkboard_color1(x, y,color):
    return render_template(
        "index.html",
        row=x,
        col=y,
        color1=color,
        color2="black"
)
@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def checkboard_color(x, y,color1,color2):
    return render_template(
        "index.html",
        row=x,
        col=y,
        color1=color1,
        color2=color2
)

if __name__ == "__main__":
    app.run(debug= True)