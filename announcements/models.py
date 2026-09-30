from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Announcement(models.Model):
    """اطلاعیه‌های مدرسه"""
    
    PRIORITY_CHOICES = [
        ('normal', 'عادی'),
        ('important', 'مهم'),
        ('urgent', 'فوری'),
    ]
    
    title = models.CharField('عنوان', max_length=200)
    content = models.TextField('متن اطلاعیه')
    priority = models.CharField('اولویت', max_length=10, choices=PRIORITY_CHOICES, default='normal')
    image = models.ImageField('تصویر', upload_to='announcements/', blank=True, null=True)
    is_published = models.BooleanField('منتشر شده', default=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='نویسنده')
    created_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    updated_at = models.DateTimeField('آخرین ویرایش', auto_now=True)
    
    class Meta:
        verbose_name = 'اطلاعیه'
        verbose_name_plural = 'اطلاعیه‌ها'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
