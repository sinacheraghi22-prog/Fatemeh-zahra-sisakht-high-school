from django.db import models


class Activity(models.Model):
    """فعالیت‌های مدرسه در چهار دسته"""
    
    CATEGORY_CHOICES = [
        ('omrani', 'عمرانی'),
        ('amoozeshi', 'آموزشی'),
        ('manfaati', 'عام‌المنفعه'),
        ('parvareshi', 'پرورشی'),
    ]
    
    title = models.CharField('عنوان', max_length=200)
    category = models.CharField('دسته‌بندی', max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField('توضیحات')
    image = models.ImageField('تصویر', upload_to='activities/', blank=True, null=True)
    date = models.DateField('تاریخ')
    is_published = models.BooleanField('منتشر شده', default=True)
    created_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    
    class Meta:
        verbose_name = 'فعالیت'
        verbose_name_plural = 'فعالیت‌ها'
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"
