from django.urls import path
from . import views
from django.contrib.auth import views as cbviews
from django.conf import settings
from django.conf.urls.static import static




app_name='food'
urlpatterns=[
path('',views.home,name='home'),
path('<int:item_id>',views.details,name='details'),
path('create_item',views.create_item,name='create_item'),
path('update/<int:id>',views.update,name='update'),
path('delete/<int:pk>',views.delete,name='delete'),
path('register',views.register,name='register'),
path('login',cbviews.LoginView.as_view(template_name='login.html'),name='login'),
path('logout',views.logout,name='logout'),
path('profile',views.profilepage,name='profile'),

]
urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



