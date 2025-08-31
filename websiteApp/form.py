from django import forms
from websiteApp.models import Contact, NewsLetter

class ContactForm(forms.ModelForm):
    subject = forms.CharField(required=False) 
    class Meta:
        model = Contact
        fields = '__all__'
        
class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'