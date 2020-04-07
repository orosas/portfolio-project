from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

def allblogs(request):
    all_blogs = Blog.objects.order_by('-pub_date')
    return render(request, 'blog/allblogs.html', {'all_blogs': all_blogs})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'blog/blog_detail.html', {'blog': blog})