from django.contrib import admin
from .models import *
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')

admin.site.register(BlogPost, BlogPostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')

admin.site.register(Category, CategoryAdmin)
