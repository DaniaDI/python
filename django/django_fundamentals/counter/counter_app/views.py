from django.shortcuts import render ,redirect 

# Create your views here.
    
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    else:
        request.session['count'] += 1

    context = {
        'count': request.session['count']  
    }
    return render(request, 'index.html', context)

def destroy(request):
    if 'count' in request.session:
     del request.session['count'] 
    return redirect('/')

def add2(request):
   if 'count' in request.session:
     request.session['count'] +=2
   else:
       request.session['count'] = 2
   return redirect('/')

def add_custom(request):
   number= int(request.POST['number'])

   if 'count' in request.session:
        request.session['count'] += number
   else:
        request.session['count'] = number
  
   return redirect('/')
   