from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import BlogPostForm
from django.core.paginator import Paginator


# View All Blog list :
def blog_list(request):
    blogs = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    paginator = Paginator(blogs, 6)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # return render(request, 'blog_list.html', {'blogs': blogs})
    return render(request, 'blog_list.html', {'page_obj': page_obj})


def recent_blog(request):
    related_blogs = BlogPost.objects.all()
    return render(request, 'blog_detail.html', {'related_blogs': related_blogs})

# View Any Specific Blog :  
def blog_detail_slug(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    related_blogs = BlogPost.objects.all() 
    return render(request, 'blog_detail.html', {'blog': blog, 'related_blogs': related_blogs})

# ## Create (Add a new Post) and Update (Update a new Post) :
# def blog_create_update(request, slug=None):
#     blog = None
#     if slug:
#         blog = get_object_or_404(BlogPost, slug=slug)  # Fetch blog if slug is provided
    
#     if request.method == "POST":
#         form = BlogPostForm(request.POST, instance=blog)  # Pass instance if updating
#         if form.is_valid():
#             form.save()
#             return redirect('blog_detail', slug=form.instance.slug) if slug else redirect('blog_list')
#     else:
#         form = BlogPostForm(instance=blog)

#     return render(request, 'blog_form.html', {'form': form, 'is_update': bool(blog)})
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Check if user is admin or staff
def is_admin_or_staff(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)

@user_passes_test(is_admin_or_staff)
def blog_create_update(request, slug=None):
    blog = None
    if slug:
        blog = get_object_or_404(BlogPost, slug=slug)

    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', slug=form.instance.slug) if slug else redirect('blog_list')
    else:
        form = BlogPostForm(instance=blog)

    return render(request, 'blog_form.html', {'form': form, 'is_update': bool(blog)})


# View Related Blogs (Assuming you have a method to get related blogs) :


# Delete Blog Post :
def blog_delete(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    
    if request.method == "POST":
        blog.delete()
        return redirect('blog_list')
    
    return render(request, 'blog_detail.html', {'blog': blog})

