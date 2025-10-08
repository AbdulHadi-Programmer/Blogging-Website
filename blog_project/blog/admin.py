from django.contrib import admin
from .models import *
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'is_published', 'category')
    list_editable = ('is_published', 'category')
    # list_editable = ('category', )

admin.site.register(BlogPost, BlogPostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','description')

admin.site.register(Category, CategoryAdmin)
