from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'date_posted')
    list_filter = ('category', 'date_posted')
    search_fields = ('title', 'content')