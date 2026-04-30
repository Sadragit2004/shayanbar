from django.urls import path,include
from .views import show_comment,show_blog_group,recently_blog,show_group_blog,BlogDetailView,show_blogList,show_title_blog,show_blog_grid

app_name = 'blog'

urlpatterns = [


    path('blog-view/',show_blogList,name='blogs'),
    path('<str:slug>/',BlogDetailView.as_view(),name='detail'),
    path('s/blog-title/',show_title_blog,name='titles'),
    path('', show_blog_grid, name='show-blog'),



]
