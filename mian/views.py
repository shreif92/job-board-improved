from django.shortcuts import render
from job.views import job_list
from job.filters import JobFilter
from django.core.paginator import Paginator
from job.models import Job


def index(request):
    job_list = Job.objects.all()

    myfilter = JobFilter(request.GET, queryset=job_list)

    # Use myfilter.qs to get the filtered queryset
    paginator = Paginator(myfilter.qs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"jobs": page_obj, 'myfilter': myfilter}

    return render(request, 'index.html', context)



# def index(request):
#     context = {'job_list': job_list}
#     return render(request, 'index.html', context)
