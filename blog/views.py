from django.shortcuts import render,get_object_or_404
from .models import Project_blog

def all_blogs(request):
    blogs = Project_blog.objects.all()
    return render(request ,'blog/all_blogs.html' , {'blogs' :blogs})

def detail(request , blog_id):
    blog = get_object_or_404(Project_blog , pk = blog_id )
    return render(request ,'blog/detail.html' , {'blog':blog})