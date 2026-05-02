from flask import Flask ,render_template,request ,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
     return render_template("form.html")

@app.route("/result" , methods=["POST","GET"])
def result():
    if request.method == 'POST':
            name = request.form["name"]
            location =request.form["location"]           
            lang =request.form["lang"]
            textarea =request.form["text"]
            return redirect(url_for("show",
            name=name ,
            location=location,
            lang=lang,
            comment=textarea
            ))
    else :
        return render_template("form.html")
    
@app.route("/show")
def show():
    name = request.args.get("name") #معناتها هات البيانات من الرابط
    location = request.args.get("location")
    lang = request.args.get("lang")
    comment = request.args.get("comment")

    return render_template(
        ("show.html"),
        name=name,
        location=location,
        lang=lang,
        comment=comment
    )

if __name__ == "__main__":
    app.run(debug=True)