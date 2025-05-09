from django.urls import path, include 
from .views import * 
# blog_create_update, blog_detail_slug, blog_detail_view

# urlpatterns = [
#     path('', home, name='home'),
#     path('', blog_list, name='blog_list'),
#     path('<slug:slug>/', blog_detail, name='blog_detail'),
#     path('create/', blog_create, name='blog_create'),
#     path('<slug:slug>/edit/', blog_update, name='blog_update'),
#     path('<slug:slug>/delete/', blog_delete, name='blog_delete'),
# ]
urlpatterns = [
    # path('', home, name='home'),  # Home page
    path('tinymce/', include('tinymce.urls')),
    path('', blog_list, name='blog_list'),  # View all blogs
    path('blogs/', blog_list, name='blog_list'),  # View all blogs
    path('blogs/<slug:slug>/', blog_detail_slug, name='blog_detail'),  # View specific blog
    path('blogs/create/', blog_create_update, name='blog_create'),  # Create new blog
    path('blogs/<slug:slug>/edit/', blog_create_update, name='blog_update'),  # Update existing blog
    path('blogs/<slug:slug>/delete/', blog_delete, name='blog_delete'),  # Delete blog
    path('blog/add/', blog_create_update, name='blog_create'),
    path('blog/edit/<slug:slug>/', blog_create_update, name='blog_update'),
]