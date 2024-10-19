import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = {
            'title': ['icontains'],       # Search by title (case-insensitive)
            'job_type': ['exact'],
            'description': ['icontains'],
            'experance': ['exact'],
            'category': ['exact'],
        }