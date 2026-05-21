from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'index.html', context)

 

def time_view(request):
    time = datetime.now()
    context = {
        "time": time.strftime("%Y-%m-%d %H:%M %p"),
        "day": time.strftime("%A"),      
        "month": time.strftime("%B"),      
        "year": time.year,                
        "hour": time.hour,                
        "minute": time.minute,             
    }
    return render(request, 'time.html', context)