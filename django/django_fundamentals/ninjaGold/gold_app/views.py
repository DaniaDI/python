from django.shortcuts import render,redirect
import random
# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
        request.session['activities']=[]
        
    context={
        'gold':request.session.get('gold',0),
        'activities':request.session.get('activities',[]),
    }

    return render(request,'index.html',context)

def process_money(request):
    if request.method == 'POST':
        building=request.POST.get('building')
        
        if building == 'farm':
         gold = random.randint(10, 20)

        elif building == 'cave':
           gold =  random.randint(5, 10)

        elif building == 'house':
          gold =  random.randint(2, 5)
 
        elif building == 'casino':
           gold =  random.randint(-50, 50)

        request.session['gold'] +=gold

              # إنشاء message
    if gold >= 0:
     message = f"<p style='color:green'>Earned {gold} gold from {building}</p>"
    else:
         message = f"<p style='color:red'>Lost {abs(gold)} gold at {building}</p>"

    activities = request.session.get("activities", [])
    activities.append(message)
    request.session['activities']=activities
    return redirect('/')

def restart(request):
        request.session['gold']=0
        request.session['activities']=[]
        return redirect('/')