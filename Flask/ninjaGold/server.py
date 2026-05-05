from flask import Flask ,render_template,redirect,session ,request
import random

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route("/")
def home():
    if 'gold'  not in session:
        session['gold']= 0
        session['activities'] = []

    return render_template("index.html", gold=session.get('gold'),
        activities=session.get('activities'))

@app.route("/process_money", methods=['POST'])
def process_money():
      
       building = request.form.get("building")

       if building == 'farm':
            gold = random.randint(10, 20)

       elif building == 'cave':
            gold = random.randint(5, 10)

       elif building == 'house':
            gold = random.randint(2, 5)
 
       elif building == 'casino':
            gold = random.randint(-50, 50)


      # تحديث الذهب
       session['gold'] += gold

               # إنشاء message
       if gold >= 0:
         message = f"<p style='color:green'>Earned {gold} gold from {building}</p>"
       else:
         message = f"<p style='color:red'>Lost {abs(gold)} gold at {building}</p>"

               # تخزين النشاط
       session['activities'].insert(0, message)

       return redirect("/")




@app.route("/restart")
def restart():
    session.clear()
    return redirect("/")






if __name__ == "__main__":
    app.run(debug= True)