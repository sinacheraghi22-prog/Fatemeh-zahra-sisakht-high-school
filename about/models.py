from django.db import models


class Dormitory(models.Model):
    """خوابگاه"""
    name = models.CharField('نام', max_length=200)
    description = models.TextField('توضیحات')
    address = models.CharField('آدرس', max_length=300, blank=True)
    phone = models.CharField('تلفن', max_length=20, blank=True)
    manager = models.CharField('مسئول خوابگاه', max_length=100, blank=True)
    image = models.ImageField('تصویر اصلی', upload_to='dormitory/', blank=True, null=True)
    created_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)
    
    class Meta:
        verbose_name = 'خوابگاه'
        verbose_name_plural = 'خوابگاه‌ها'
    
    def __str__(self):
        return self.name
    
    @property
    def total_capacity(self):
        """ظرفیت کل خوابگاه"""
        total = 0
        for block in self.blocks.all():
            total += block.total_capacity
        return total
    
    @property
    def total_suites(self):
        """تعداد کل سوییت‌ها"""
        return sum(block.suites.count() for block in self.blocks.all())


class Block(models.Model):
    """بلوک خوابگاه"""
    dormitory = models.ForeignKey(
        Dormitory, 
        on_delete=models.CASCADE, 
        related_name='blocks',
        verbose_name='خوابگاه'
    )
    name = models.CharField('نام بلوک', max_length=100)
    description = models.TextField('توضیحات', blank=True)
    manager = models.CharField('مسئول بلوک', max_length=100, blank=True)
    order = models.PositiveIntegerField('ترتیب نمایش', default=0)
    
    class Meta:
        verbose_name = 'بلوک'
        verbose_name_plural = 'بلوک‌ها'
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.dormitory.name} - {self.name}"
    
    @property
    def total_capacity(self):
        """ظرفیت کل بلوک"""
        return sum(suite.capacity for suite in self.suites.all())
    
    @property
    def suite_count(self):
        """تعداد سوییت‌های بلوک"""
        return self.suites.count()


class Suite(models.Model):
    """سوییت خوابگاه"""
    block = models.ForeignKey(
        Block, 
        on_delete=models.CASCADE, 
        related_name='suites',
        verbose_name='بلوک'
    )
    number = models.CharField('شماره سوییت', max_length=20)
    capacity = models.PositiveIntegerField('ظرفیت', default=6)
    description = models.TextField('توضیحات', blank=True)
    image = models.ImageField('تصویر', upload_to='suites/', blank=True, null=True)
    order = models.PositiveIntegerField('ترتیب نمایش', default=0)
    
    class Meta:
        verbose_name = 'سوییت'
        verbose_name_plural = 'سوییت‌ها'
        ordering = ['order', 'number']
    
    def __str__(self):
        return f"{self.block.name} - سوییت {self.number}"
