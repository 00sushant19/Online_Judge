from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Question,Submission, User

admin.site.register(Question)
admin.site.register(User)
admin.site.register(Submission)