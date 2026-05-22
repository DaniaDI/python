from django.shortcuts import render , redirect

# Create your views here.
def index(request):
    
    return render (request,'index.html')


def result(request):
        if request.method =='POST':
                request.session['username'] = request.POST['name']
                request.session['location'] = request.POST['location']
                request.session['lang']     = request.POST['lang']
                request.session['comment']  = request.POST['comment']
                return redirect('/result/')   # ← redirect بعد POST

    # GET request → اقرئي من session
        context = {
                'username': request.session.get('username', ''),
                'location': request.session.get('location', ''),
                'lang':     request.session.get('lang', ''),
                'comment':  request.session.get('comment', ''),
    }
        return render(request, 'result.html', context)