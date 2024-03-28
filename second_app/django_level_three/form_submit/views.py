from django.shortcuts import render
from . import forms

# Create your views here.
def form_new(request):
   form=forms.myform()
   return render(request,'form.html',{'form':form})