from django.contrib import admin
from .models import Article , Comment , Feedback , Subject

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Feedback)
admin.site.register(Subject)