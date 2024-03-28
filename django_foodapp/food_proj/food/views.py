from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item
from .forms import item_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registration_form
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    item_list=item.objects.all()
    context={
        'items':item_list
    }
    return render(request,'home.html',context)


def details(request,item_id):
    snack=item.objects.get(pk=item_id)
    context={
        'snack':snack
    }

    return render(request,'details.html',context)
@login_required
def create_item(request):
    form=item_form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:home')
    
    return render(request,'item_create.html',{'form':form})


def update(request,id):
    itm=item.objects.get(id=id)
    form=item_form(request.POST or None,instance=itm)

    if form.is_valid():
        form.save()
        return redirect('food:home')
    return render(request,'item_create.html',{'form':form,'itm':itm})

def delete(request,pk):
    itm=item.objects.get(id=pk)
    if request.method=='POST':
     itm.delete()
     return redirect('food:home')
    return render(request,'delete.html',{'itm':itm})

def register(request):
    if request.method=='POST':
     form=registration_form(request.POST)
     if form.is_valid():
        form.save()
        username=form.cleaned_data.get('username')
        messages.success(request,f'Welcome {username}... You successfully Login')
        return redirect('food:login')
    else:
       form=registration_form() 

    return render(request,'register.html',{'form':form})   


def logout(request):
       auth.logout(request)

       return redirect('food:home')
@login_required
def profilepage(request):
    return render(request,'profile.html')


   
