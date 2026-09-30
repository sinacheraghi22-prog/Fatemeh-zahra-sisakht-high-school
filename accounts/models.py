
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """کاربر سفارشی با نقش"""
    
    ROLE_CHOICES = [
        ('admin', 'مدیر'),
        ('teacher', 'دبیر'),
        ('student', 'دانش‌آموز'),
    ]
    
    role = models.CharField('نقش', max_length=20, choices=ROLE_CHOICES, default='student')
    phone = models.CharField('شماره تماس', max_length=15, blank=True)
    national_code = models.CharField('کد ملی', max_length=10, blank=True)
    avatar = models.ImageField('عکس پروفایل', upload_to='avatars/', blank=True, null=True)
    
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
    
    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.get_role_display()})"
    
    @property
    def is_admin_role(self):
        return self.role == 'admin'
    
    @property
    def is_teacher(self):
        return self.role == 'teacher'
    
    @property
    def is_student(self):
        return self.role == 'student'
