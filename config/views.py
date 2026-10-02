from django.shortcuts import render
from announcements.models import Announcement
from about.models import SiteStat


def home(request):
    latest_announcements = Announcement.objects.filter(is_published=True)[:3]
    site_stats = SiteStat.objects.filter(is_active=True)
    return render(request, 'home.html', {
        'latest_announcements': latest_announcements,
        'site_stats': site_stats,
    })
