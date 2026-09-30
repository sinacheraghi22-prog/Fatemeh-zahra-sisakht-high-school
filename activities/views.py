from django.shortcuts import render, get_object_or_404
from .models import Activity


def activity_list(request):
    category = request.GET.get('category', '')
    activities = Activity.objects.filter(is_published=True)

    if category:
        activities = activities.filter(category=category)

    context = {
        'activities': activities,
        'current_category': category,
        'categories': Activity.CATEGORY_CHOICES,
    }
    return render(request, 'activities/list.html', context)


def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk, is_published=True)
    return render(request, 'activities/detail.html', {
        'activity': activity
    })
