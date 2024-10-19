from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


job_type = {
    'full-time': 'Full-time',
    'part-time': 'Part-time',
    'freelance': 'Freelance',
    'internship': 'Internship',
    'temporary': 'Temporary',
    'volunteer': 'Volunteer',
    'student': 'Student',
    'other': 'Other',
}


class Job(models.Model):
    owner = models.name = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=50, choices=job_type)
    description = models.TextField(max_length=500, blank=True, null=True)
    published_at = models.DateField(auto_now=True)
    vacnecy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experance = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,)
    image = models.ImageField(upload_to='jobs/', null=True,blank=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title
    


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length=200)
    cv = models.FileField(upload_to='apply/', max_length=100)
    coverlitter = models.TextField(max_length=500)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

