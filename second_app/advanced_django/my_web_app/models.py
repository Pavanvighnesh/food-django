from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class post(models.Model):
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()
    creation_date=models.DateTimeField(default=timezone.now())
    publication_date=models.DateTimeField(blank=True,null=True)


    def publish(self):
        self.publication_date=timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)  

    def get_absolute_url(self):
        return self.reverse('post_detail',kwargs={'pk':self.pk}) 
    
    def __str__(self):
        return self.title
    

class comment(models.Model):
    post=models.ForeignKey('my_web_app.post',related_name='comments',on_delete=models.CASCADE)   
    author=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now())
    approved_comment=models.BooleanField(default=False) 

    def approve(self):
        self.approved_comment=True
        self.save()

    def get_absolute_url(self):
        return self.reverse('post_list')    

    def __str__(self):
        return self.text    
