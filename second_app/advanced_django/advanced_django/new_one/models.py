from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author=models.CharField(max_length=100)
    date=models.DateField()


    def __str__(self):
        return self.book_name
class person(models.Model):
    name=models.CharField(max_length=200,default='hello')
    fav_book=models.ForeignKey(Book,related_name='person',on_delete=models.CASCADE)    

    def __str__(self):
        return self.name
