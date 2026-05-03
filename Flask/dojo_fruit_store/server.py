from flask import Flask, render_template, request, redirect ,url_for
from datetime import datetime
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    fruite1= int(request.form.get("strawberry" ,0))
    fruite2= int(request.form.get("raspberry",0))
    fruite3= int(request.form.get("apple",0))

# 2. حساب المجموع الكلي
    total_items =   fruite1 +  fruite2 + fruite3
    current_date = datetime.now().strftime("%B %d, %Y %I:%M %p")#%Y: السنة كاملة (2026).

    first_name=request.form.get("first_name")
    last_name=request.form.get("last_name")
    student_id=request.form.get("student_id")
    return redirect(url_for("show",
                    strawberry=fruite1 ,
                    raspberry=fruite2 ,
                    apple =fruite3 ,
                    first_name =first_name ,
                    last_name =last_name,
                    student_id=student_id,
                    total=total_items,
                    date = current_date))

@app.route('/show')         
def show():
     
    fruite1 = request.args.get("strawberry") #معناتها هات البيانات من الرابط
    fruite2 = request.args.get("raspberry")
    fruite3 = request.args.get("apple")
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")
    student_id = request.args.get("student_id")
    total=request.args.get("total")
    date=request.args.get("date")

    return render_template(
        "checkout.html",
         strawberry=fruite1 ,
                    raspberry=fruite2 ,
                    apple =fruite3 ,
                    first_name =first_name ,
                    last_name =last_name,
                    student_id=student_id,
                    total=total,
                    date=date
    )
    

@app.route('/fruits')         
def  fruits():
    return render_template("fruits.html")

#friute
if __name__=="__main__":   
    app.run(debug=True)    