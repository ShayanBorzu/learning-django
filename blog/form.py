from django import forms
from websiteApp.models  import Contact
from .models import Comment

class NameForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label='Email')
    subject = forms.CharField(label="Subject", max_length=100)
    message = forms.CharField(label="Message", widget=forms.Textarea)
    
    
class BlogContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'subject', 'message']