from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models

def first(request):
   return render(request,'base.html')
    #return HttpResponse("hello all")

class cbview(View):
    def get(self,request):
        return HttpResponse("Class Based Views are nice to use!!!")
class indextemplate(TemplateView):
    template_name='index.html'    

def  template(request):
    return render(request,'index.html')



class listview(ListView):
    #context_object_name='books'
    model=models.Book
    template_name='new_one/listview.html'
   
