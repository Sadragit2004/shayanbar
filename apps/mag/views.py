from django.shortcuts import render,redirect
from django.urls import reverse

from django.core.paginator import Paginator
from .models import Blog,Group_blog,Meta_tag_model,Comment,Meta_tag_model_group
from django.views import View


# Create your views here.

def show_blogList(request):

    blogs = Blog.objects.filter(is_active = True).order_by('-register_data')
    return render(request,'blog_app/blog_main.html',{'blogs':blogs})



def show_title_blog(request):

    blogs = Blog.objects.filter(is_active = True).order_by('-register_data')
    return render(request,'blog_app/title_blog.html',{'blogs':blogs})




def show_blog_grid(request):

    
    blogs = Blog.objects.filter(is_active=True).order_by('-register_data')

    paginator = Paginator(blogs, 10)  # نمایش ۱۰ پست در هر صفحه
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog_app/blog_list.html', {
        'page_obj': page_obj,
        'blogs': blogs,
    })





class BlogDetailView(View):

    def get(self,request,*args, **kwargs):

        slug = kwargs['slug']
        # group = Group_blog.objects.filter(slug = slug).first()پ

        blog = Blog.objects.filter(slug = slug).first()



        if blog:
            blog.view+=1
            blog.save()

        Metas = Meta_tag_model.objects.filter(blog = blog).first()

        return render(request,'blog_app/blog_detail.html',{'blog':blog,'meta':Metas})





def show_group_blog(request):

    groups = Group_blog.objects.filter(is_active = True).order_by('-register_data')
    return render(request,'blog_app/groups.html',{'groups':groups})





def recently_blog(request):

    blogs = Blog.objects.filter(is_active = True).order_by('-register_data')
    return render(request,'blog_app/recently_blog.html',{'blogs':blogs})





def show_blog_group(request,*args, **kwargs):

    slug = kwargs['slug']
    group = Group_blog.objects.filter(slug = slug).first()
    blogs = Blog.objects.filter(is_active = True).order_by('-register_data')
    return render(request,'blog_app/show_by_group.html',{'blogs':blogs,'groups':group})



def show_comment(request,*args, **kwargs):


        comments = Comment.objects.filter(is_active = True).order_by('-register_data')
        return render(request,'blog_app/comment.html',{'comments':comments})

