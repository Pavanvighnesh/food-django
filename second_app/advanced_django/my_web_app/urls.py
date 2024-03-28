from django.urls import path
from . import views

urlpatterns=[
    path('about',views.aboutview.as_view(),name='about'),
    path('',views.postlistview.as_view(),name='post_list'),
    path('post/detail/<pk>/',views.postdetailview.as_view(),name='post_detail'),
    path('post/new',views.createpostview.as_view(),name="post_create"),
    path('post/<pk>/remove',views.deletepostview.as_view(),name='post_delete'),
    path('post/<pk>/edit',views.updatepostview.as_view(),name='post_update'),
    path('path/drafts',views.draftlistview.as_view(),name="post_draft"),
    path('path/<pk>/comment',views.add_comment_to_post,name='add_comment'),
    path('comment/<pk>/approved',views.comment_approve,name='comment_approve'),
    path('comment/<pk>/remove',views.comment_remove,name="remove_comment"),
    path('post/<pk>/publish',views.post_publish,name='publish_post'),



    
]