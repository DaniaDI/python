from flask import Flask, session, render_template,request ,redirect

app = Flask(__name__)
app.secret_key = 'secret123'

@app.route('/')
def index():
    # visits
    if 'visits' not in session:
        session['visits'] = 1 # اذا اول مرة 
    else:
        session['visits'] += 1 

    # إذا أول مرة
    if 'count' not in session:
        session['count'] = 1
    else:
        session['count'] += 1

    return render_template('index.html')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/add2')
def add2():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 2
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

@app.route('/add_custom', methods=['POST'])
def add_custom():
    num = int(request.form['number'])
    session['count'] += num
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)