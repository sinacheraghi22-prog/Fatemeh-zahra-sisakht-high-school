from django.contrib import admin
from .models import Dormitory, Block, Suite, SiteStat


class SuiteInline(admin.TabularInline):
    model = Suite
    extra = 1
    fields = ('number', 'capacity', 'order', 'description')


class BlockInline(admin.TabularInline):
    model = Block
    extra = 1
    fields = ('name', 'order', 'manager', 'description')


@admin.register(Dormitory)
class DormitoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'manager', 'total_suites', 'total_capacity')
    search_fields = ('name', 'manager')
    inlines = [BlockInline]

    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('name', 'description', 'image')
        }),
        ('اطلاعات تماس', {
            'fields': ('address', 'phone', 'manager')
        }),
    )


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'dormitory', 'manager', 'suite_count', 'total_capacity', 'order')
    list_filter = ('dormitory',)
    search_fields = ('name', 'manager')
    inlines = [SuiteInline]
    ordering = ('dormitory', 'order')


@admin.register(Suite)
class SuiteAdmin(admin.ModelAdmin):
    list_display = ('number', 'block', 'capacity', 'order')
    list_filter = ('block', 'block__dormitory')
    search_fields = ('number',)
    ordering = ('block', 'order')


@admin.register(SiteStat)
class SiteStatAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'icon', 'order', 'is_active')
    list_editable = ('value', 'order', 'is_active')
    list_filter = ('is_active',)
    ordering = ('order',)
