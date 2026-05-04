from flask import Flask, session, render_template,request ,redirect 
import random

app = Flask(__name__)
app.secret_key = 'dania123'

@app.route("/")
def home():
  if 'num' not in session: #اختار رقم عشوائي ويخزنه
    session['num'] = random.randint(1, 100)    
    session['game_over'] = False    
    session['attempts'] = 0
    session['result'] = ""

  return render_template("index.html", result=session.get('result') ,game_over=session.get('game_over'),attempts=session.get('attempts'))
    
@app.route('/guess', methods=['POST'])
def guess():
 user_input = int(request.form.get('num'))
 server = int(session['num'])
 session['attempts'] = session.get('attempts', 0) + 1

 if session['attempts'] >= 5 and user_input != server:#إذا المستخدم حاول 5 مرات ولسه ما خمن الرقم الصحيح
        session['result'] = f'you loose'
        session['game_over'] = True

 if user_input < server:
    session['result'] = "Too Low"
 elif user_input > server:
    session['result'] = "Too High"
 else:
    session['result'] = "Correct!"
    session['game_over'] = True   # فقط هنا توقف اللعبة
 return redirect('/')



@app.route("/restart")
def restart():
    session.clear()
    return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)