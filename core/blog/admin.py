from django.contrib import admin
from .models import Post, Category


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','status','author','created_date')
    list_filter = ('status',)
    search_fields = ("author",)
    ordering = ("-created_date",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Post)
admin.site.register(Category)