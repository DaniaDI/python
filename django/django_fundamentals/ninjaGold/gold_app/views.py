from django.shortcuts import render,redirect
import random
# Create your views here.
def index(request):

   if 'condition' not in request.session:
    
       return render(request,'setup.html')

   if 'gold' not in request.session:
        request.session['gold']=0
        request.session['moves'] = 0
        request.session['game_over'] = False
        request.session['result'] = ""
        request.session['activities']=[]
        
   context={
        'gold':request.session.get('gold',0),
        'activities':request.session.get('activities',[]),
        'target_gold': request.session.get('target_gold', 100),
        'max_moves': request.session.get('max_moves', 10), # جلب عدد الحركات المخصص لليوزر
        'moves': request.session.get('moves', 0),# عداد الخطوات الحالي
        'game_over': request.session.get('game_over', False),
        'result': request.session.get('result', ""),
    }

   return render(request,'index.html',context)

def process_money(request,building):
    if request.method == 'POST':
        if building == 'setup':
            request.session['target_gold'] = int(request.POST.get('target_gold', 100))
            request.session['max_moves'] = int(request.POST.get('max_moves', 10))
            request.session['condition'] = True
            return redirect('/')
        
        if request.session.get('game_over', False):
            return redirect('/')
        #  زيادة عداد الحركات وحساب الذهب
        request.session['moves'] = request.session.get('moves', 0) + 1
        current_moves = request.session['moves']
        gold = 0

        # building=request.POST.get('building')
        
        if building == 'farm':
         gold = random.randint(10, 20)

        elif building == 'cave':
           gold =  random.randint(5, 10)

        elif building == 'house':
          gold =  random.randint(2, 5)
 
        elif building == 'casino':
           gold =  random.randint(-50, 50)

        request.session['gold'] +=gold
        current_gold = request.session['gold']
        # جلب الشروط المخصصة المخزنة للمقارنة وكتابة الرسالة
        max_moves = request.session.get('max_moves', 10)
        target_gold = request.session.get('target_gold', 100)

              # إنشاء message
        if gold >= 0:
           message = f"<p style='color:green'>Earned {gold} gold from {building}</p>"
        else:
            message = f"<p style='color:red'>Lost {abs(gold)} gold at {building}</p>"

        activities = request.session.get("activities", [])
        activities.append(message)
        request.session['activities']=activities

        if current_gold >= target_gold and current_moves <= max_moves:
            request.session['game_over'] = True
            request.session['result'] = f" Congratulations! You won!{current_gold}  {current_moves} "
        elif current_gold < 0:
            request.session['game_over'] = True
            request.session['result'] = "Game Over!"
        elif current_moves >= max_moves and current_gold < target_gold:
            request.session['game_over'] = True
            request.session['result'] = f"Out of moves! Game Over.{target_gold} ."

    return redirect('/')

      
def restart(request):
        # request.session['gold']=0
        # request.session['activities']=[]
        request.session.flush()
        return redirect('/')