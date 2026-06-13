from django.shortcuts import render,redirect
from .forms import CourseForm
from .models import Course , Description
# Create your views here.
def index(request):
    
    if request.method == 'POST':
            form =CourseForm(request.POST)
            if form.is_valid():
                course_name = form.cleaned_data['name']
                course_desc = form.cleaned_data['desc']
                
                # خلق جدول الوصف أولاً ثم ربطه بجدول الكورس (One-to-One)
                new_desc = Description.objects.create(desc=course_desc)
                Course.objects.create(name=course_name, course_desc=new_desc)
                return redirect('course_index')
    else:
            
            form = CourseForm()

    context={
                "form":form,
                'all_courses':Course.objects.all()  
    }
        
    return render(request,'index.html',context)
  

def course_delete(request,id):

    course = Course.objects.get(id=id)

    if request.method == "POST":
        course.course_desc.delete()
        course.delete()
        return redirect('course_index')

    # GET  عرض صفحة التأكيد مع Name و Description
    return render(request, 'destroy.html', {'course': course})