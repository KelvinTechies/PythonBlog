from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginin, name='login'),
    path('create-post/', views.createblog, name='create-blog'),
    path('view-post/', views.viewblog, name='viewpost'),
    path('create-blog/', views.createpost, name='create-post'),    
    path('create-comment/<str:pk>/', views.comment, name='comment'),    
    path('view-blog/', views.viewpost, name='viewblog'),
    path('Education/', views.Education, name='education'),
    path('sports/', views.sports, name='sports'),
    path('edit-post/<str:pk>/', views.editblog, name='edit-post'),
    path('edit-blog/<str:pk>/', views.editpost, name='edit-blog'),
    path('delete-post/<str:pk>/', views.deleteblog, name='delete-post'),
    path('delete-blog/<str:pk>/', views.deletepost, name='delete-blog'),
    path('description/<str:pk>/', views.description, name='description'),
    path('details/<str:pk>/', views.details, name='details'),
    path('blog-details/<str:pk>/', views.detailsblog, name='blog-details'),
    path('create-comment-blog/<str:pk>/', views.blogcomment, name='create-comment-blog')

]