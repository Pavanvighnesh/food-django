from django.urls import path
from . import views



app_name='food'
urlpatterns=[
path('',views.home,name='home'),
path('<int:item_id>',views.details,name='details'),
path('create_item',views.create_item,name='create_item'),
path('update/<int:id>',views.update,name='update'),
path('delete/<int:pk>',views.delete,name='delete')

]