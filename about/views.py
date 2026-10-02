from django.shortcuts import render, get_object_or_404
from .models import Dormitory, Block


def dormitory_detail(request):
    """صفحه خوابگاه"""
    dormitory = Dormitory.objects.first()  # فقط یه خوابگاه داریم
    return render(request, 'about/dormitory.html', {
        'dormitory': dormitory
    })


def block_detail(request, pk):
    """صفحه جزئیات یه بلوک"""
    block = get_object_or_404(Block, pk=pk)
    return render(request, 'about/block.html', {
        'block': block
    })
