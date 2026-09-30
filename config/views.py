from django.shortcuts import render
from announcements.models import Announcement


def home(request):
    latest_announcements = Announcement.objects.filter(is_published=True)[:3]
    return render(request, 'home.html', {
        'latest_announcements': latest_announcements
    })
