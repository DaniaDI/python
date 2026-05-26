
from django.shortcuts import render, redirect
import random

def index(request):
   
    if "num" not in request.session:
        request.session["num"] = random.randint(1, 100)
        request.session["game_over"] = False
        request.session["attempts"] = 0
        request.session["result"] = ""
        request.session["won"] = False

   
    context = {
        "result": request.session.get("result"),
        "game_over": request.session.get("game_over"),
        "attempts": request.session.get("attempts"),
        "won": request.session.get("won"),
    }

  
    return render(request, "index.html", context)


def guess(request):
    user_input = int(request.POST["num"])
    server = int(request.session["num"])
    request.session["attempts"] = request.session.get("attempts", 0) + 1

   
    if request.session["attempts"] >= 5 and user_input != server:
        request.session["result"] = "You Lose! The number was {server}."  
        request.session["game_over"] = True
        request.session["won"] = False
  
    else:
        
        if user_input < server:
            request.session["result"] = "Too Low"
        elif user_input > server:
            request.session["result"] = "Too High"
        else :
            request.session["result"] = "Correct!"
            request.session["game_over"] = True
            request.session["won"] = True
            

    return redirect("/")


def restart(request):
  
  game_keys = ["num", "game_over", "attempts", "result", "won"]

    # 2. نمر عليها واحداً تلو الآخر ونحذفها إذا كانت موجودة عشان ما يحذف كمان البورد 
  for key in game_keys:
        if key in request.session:
            del request.session[key]

        return redirect("/")
   


def save_score(request):
    """حفظ اسم الفائز وعدد محاولاته في قائمة المتصدرين"""
    if request.method == "POST":
        player_name = request.POST.get("player_name", "")
        attempts = request.session.get("attempts", 0)

        leaderboard = request.session.get("leaderboard", [])
        leaderboard.append({"name": player_name, "attempts": attempts})
        request.session["leaderboard"] = leaderboard

        request.session["won"] = False

    return redirect("/leaderboard/")

def leaderboard(request):
    """عرض صفحة لوحة الصدارة"""
    context = {
        "leaderboard": request.session.get("leaderboard", [])
        }

    return render(request,'leaderboard.html',context)