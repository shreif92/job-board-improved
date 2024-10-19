from django.contrib import admin

# Register your models here.
from .models import Job, Category,Apply

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Apply)




# This is a normal comment
# ! This is a highlighted comment                    "مهم"
# ? Is this the correct implementation?              "سؤال"
# !! Deprecated function                             "تحزير"
# TODO: Refactor this code                       "تعليمات (To-Do)"
# ~ This code is commented out ~                "إلغاء (Strike-through)"
