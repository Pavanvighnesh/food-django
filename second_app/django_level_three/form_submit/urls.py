from django.urls import path
from django.conf import urls
from . import views


urlpatterns=[
    path('form_new',views.form_new)
]