from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm, Jobform
from django.contrib.auth.decorators import login_required
from .filters import JobFilter


def job_list(request):
    job_list = Job.objects.all()

    myfilter = JobFilter(request.GET, queryset=job_list)

    # Use myfilter.qs to get the filtered queryset
    paginator = Paginator(myfilter.qs, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"jobs": page_obj, 'myfilter': myfilter}     # {"uses in the templates": the variable}
    return render(request, 'job_list.html', context)


@login_required
def job_details(request, slug):
    # first id is the one in the database but the seconde one is the id which i send it
    job_details = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job_details
            application.save()
            return redirect('jobs:job_list')
    else:
        form = ApplyForm()

    context = {"job":job_details, 'form':form}
    return render(request, 'job_details.html',context)


@login_required
def add_job(request):
    if request.method == 'POST':
        form = Jobform(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = Jobform()
    context = {'form':form}
    return render(request, 'add_job.html', context)
