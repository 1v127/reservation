from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    title=models.CharField(max_length=20)

    def __str__(self):
        return  self.title

    class Meta:
        abstract=True


class Education(BaseModel):
    pass


class Skill(BaseModel):
    pass

ResumeSkill
class Sex(BaseModel):
    pass


class Resume(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    name=models.CharField(max_length=50)
    family=models.CharField(max_length=50)
    resume_file=models.FileFild(blank=True, null=True, upload_to='media/pictures/no-img.jpg')
    address=models.CharField(max_length=200, blank=True, null=True)
    age=models.PositiveIntegerField(blank=True)
    sex=models.ForeignKey(Sex, on_delete=models.SET_NULL, null=True, related_name='sex')
    linkedin_url=models.URLField(blank=True)

    def __str__(self):
        return  self.user.id

class ResumeSkill(models.Model):
    resume=models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='resume_skill')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill')
    level=models.PositiveIntegerField(default=5)

    def __str__(self):
        return  self.skill.title