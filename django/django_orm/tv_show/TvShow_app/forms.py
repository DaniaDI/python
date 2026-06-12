from django import forms
from .models import Show

class ShowForm(forms.ModelForm):
    class Meta:
        model = Show # نربط الفورم بموديل الـ Show
        fields=['title','network','release_date','desc'] # fields wants in form

    def clean_title(self):# problem title->unique
        typing = self.cleaned_data.get('title', '').strip()# give me the clean title or data user typing
        if len(typing) < 2:
          raise forms.ValidationError("Title must be at least 2 characters long.")
        # check unique:
            # 2. التحقق من عدم التكرار 
        show = self.instance   
        title_exists = Show.objects.filter(title__iexact=typing)
        
        # إذا كنا في حالة تعديل، نستبعد المسلسل الحالي باستخدام اسمه الجديد show
        if show and show.pk:
            title_exists = title_exists.exclude(pk=show.pk)
            
        if title_exists.exists(): 
            raise forms.ValidationError("A TV show with this title already exists.")
            
        return typing