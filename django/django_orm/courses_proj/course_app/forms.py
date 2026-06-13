from django import forms

class CourseForm(forms.Form):
    name = forms.CharField(max_length=255, label="Course Name")
    desc = forms.CharField(widget=forms.Textarea, label="Description")

    def clean_name(self):
        typing = self.cleaned_data.get('name', '').strip()
        if len(typing) <= 5:
            raise forms.ValidationError("Name must be more than 5 characters long.")
        return typing

    def clean_desc(self):
        typing = self.cleaned_data.get('desc', '').strip()
        if len(typing) <= 15:
            raise forms.ValidationError("Description must be more than 15 characters long.")
        return typing