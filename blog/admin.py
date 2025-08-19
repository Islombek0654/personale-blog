from django.contrib import admin
from .models import Category, Blog, BlogTopic, ContactMessage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at", "category"]


@admin.register(BlogTopic)
class BlogTopicAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "blog"]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')
    list_filtыer = ('sent_at',)
    search_fields = ('name', 'email', 'subject', 'message')
