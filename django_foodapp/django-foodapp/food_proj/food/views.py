from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item
from .forms import item_form

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
   
