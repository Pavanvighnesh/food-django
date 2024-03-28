from django import forms
from my_web_app.models import post,comment



class postForm(forms.ModelForm):

    class Meta():
        model=post
        fields=('author','text','title')

        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class commentForm(forms.ModelForm):
    class Meta():
        model=comment
        fields=('author','text')    

        widgets={
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }    