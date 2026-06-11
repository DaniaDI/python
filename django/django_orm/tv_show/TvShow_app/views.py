from django.shortcuts import render,redirect
from .models import Show
# Create your views here.

def index(request):
    show_table=Show.objects.all()
    context={
        'all_shows':show_table
    }
    return render(request,'index.html',context)

def show_new(request):#لعرض  الفورم فقط
    return render(request,'show_new.html')
    
def show_create(request):#لاستقبال البيانات وحفظها فقط
    if request.method == 'POST':
        title=request.POST['title']
        network=request.POST['network']
        release_date=request.POST['date']
        desc=request.POST['desc']

        create_show= Show.objects.create(title=title,network=network,release_date=release_date,desc=desc)
        return redirect(f'/shows/{create_show.id}')

    return redirect('/shows/new')


def show_read(request,id):
    show=Show.objects.get(id=id)
    context={
         "show":show
     }
    return render(request,'show_read.html',context)

def show_delete(request, id):
    if request.method == "POST":
        try:
            show_to_delete = Show.objects.get(id=id)
            show_to_delete.delete()  
        except Show.DoesNotExist:
            pass 
    return redirect('/shows/')

def show_edit(request, id):#للعرض فقط
    show_to_edit = Show.objects.get(id=id)
    context={
        'show':show_to_edit
    }
    return render(request, 'update.html',context)


def show_update(request, id):
    if request.method == "POST":
        show = Show.objects.get(id=id)
        
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['date']
        show.desc = request.POST['desc']
        show.save()
        
        return redirect(f'/shows/{show.id}')
    return redirect(f'/shows/{id}/')