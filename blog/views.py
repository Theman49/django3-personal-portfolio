from django.shortcuts import render, get_object_or_404
from .models import ProjectBlog

def all_blogs(request):
    #project = ProjectBlog.objects.order_by('-date')[:2]
    project = ProjectBlog.objects.all()
    return render(request, 'blog/all_blogs.html', {'project':project})

def detail(request, blog_id):
    blog = get_object_or_404(ProjectBlog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})
