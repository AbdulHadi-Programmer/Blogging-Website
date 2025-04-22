# from django.db import models
# from django.utils.text import slugify
# from ckeditor.fields import RichTextField

# # Create your models here.
# class BlogPost(models.Model):
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True, blank=True)
#     content = RichTextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now = True)
    
#     def save(self, *args, **kwargs):
#         if not self.slug:  # Generate slug only if it's empty
#             self.slug = slugify(self.title)  
#         super().save(*args, **kwargs)  # ✅ Correct usage

#     def __str__(self):
#         return self.title
    
from django.db import models
from django.utils.text import slugify
# from ckeditor.fields import RichTextField

# Category model for grouping posts
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

from tinymce.models import HTMLField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")
    summary = models.TextField(max_length=250, null=True, blank=True)
    content = HTMLField()
    # content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)  # helpful for hiding drafts
    cover_image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
