from django.contrib import admin
from .models import Activity


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'is_published')
    list_filter = ('category', 'is_published', 'date')
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'category', 'description', 'image', 'date')
        }),
        ('وضعیت', {
            'fields': ('is_published', 'created_at')
        }),
    )
