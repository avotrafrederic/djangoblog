from django import forms
from .models import Article
class BlogPost(forms.Form):
    title = forms.CharField(max_length=50,required=True)
    auteur = forms.CharField(max_length=50,required=True)
    description = forms.CharField(widget=forms.Textarea())

class Form(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "auteur",
            "description"
        ]
        widget = {"description":forms.Textarea()}
