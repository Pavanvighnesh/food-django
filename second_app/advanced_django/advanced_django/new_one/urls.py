from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns=[
    path('welcome',views.first,name="first"),
    path('cbviews',views.cbview.as_view()),
    path('templates',views.indextemplate.as_view()),
    path('template',views.template),
    path('listview',views.listview.as_view())

]
# def dashboard(request):
#     my_record=Record.objects.all()
#     context={'record':my_record}
#     return render(request,'dashboard.html',context=context)