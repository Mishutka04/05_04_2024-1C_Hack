from django import forms
from staff_application.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        widgets = {'hr': forms.HiddenInput(),
                   'stage': forms.HiddenInput(),
                   'resume': forms.HiddenInput(),
                   'comment': forms.Textarea(attrs={"class": "form-control", "placeholder": "Комментарий"})}
