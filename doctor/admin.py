from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Resume)
admin.site.register(models.Skill)
admin.site.register(models.Education)
admin.site.register(models.Sex)
admin.site.register(models.ResumeSkill)
