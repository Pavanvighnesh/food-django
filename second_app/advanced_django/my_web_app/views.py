from django.utils import timezone
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import post,comment
from django.urls import reverse_lazy
from .forms import postForm,commentForm
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)

# Create your views here.
class aboutview(TemplateView):
    template_name='about.html'

class postlistview(ListView):
    model=post

    def get_queryset(self):
        return post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')   

class  postdetailview(DetailView):
    model=post    

class createpostview(LoginRequiredMixin, CreateView):
    login_url='/login/'
    redirect_field_name='detail.html'
    form_class=postForm
    model=post    

class updatepostview(LoginRequiredMixin, UpdateView):
    login_url='/login/'
    redirect_field_name='detail.html'
    form_class=postForm
    model=post       
    

class deletepostview(LoginRequiredMixin, DeleteView):
    model=post
    success_url=reverse_lazy('post_list')


class draftlistview(LoginRequiredMixin, ListView):
    login_url='/login/'
    redirect_field_name='post_list.html'
    model=post

    def get_queryset(self):
        return post.objects.filter(published_date__isnull=True).order_by('created_date') 




@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(post,pk=pk)
    if request.method=="POST":
        form=commentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_details',pk=post.pk)
        else:
            form=commentForm()
    return render(request,'comment_form.html',{'form':form})    


@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(comment,pk=pk)
    comment.approve()
    return redirect('post_details',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)
@login_required

def post_publish(request,pk):
    post=get_object_or_404(post,pk=pk)
    post.publish
    return redirect('post_detail',pk=pk)

# def login(request):
#     return render(request,'login.html')


            
