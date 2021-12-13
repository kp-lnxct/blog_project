from django.urls import path,include
from . import  views
from  .views import PostCreateView, PostDetailView, PostListView, PostUpdateView, PostDeleteView

urlpatterns = [
    # path('', views.home_page,name='home_page'),
    path('',PostListView.as_view(), name='home_page'),
    path('about/',views.about_page,name='about'),

    path('post/<int:pk>/',PostDetailView.as_view(), name='post_detail'),
    path('post/new/',PostCreateView.as_view(),name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    path('post_like/<int:pk>', views.like, name='post_like')
    


]
