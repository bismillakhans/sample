from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.utils.html import escape, mark_safe
# Create your models here.
class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'polus'),
      (2, 'company'),
      (3, 'department'),

  )

  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)



class Rule(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.get_username(), filename)


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    rule = models.ForeignKey(Rule, on_delete=models.CASCADE,null=True)
    resume = models.FileField('Upload Resumes', upload_to=user_directory_path)
    name = models.CharField('Name', max_length=255, null=True, blank=True)
    email = models.CharField('Email', max_length=255, null=True, blank=True)
    mobile_number = models.CharField('Mobile Number',max_length=1000, null=True, blank=True)
    skills = models.CharField('Skills', max_length=1000, null=True, blank=True)
    full_data = models.CharField('full_data', max_length=2000, null=True, blank=True)
    declaration = models.CharField('declaration', max_length=1000, null=True, blank=True)
    achievemnets = models.CharField('achievemnets', max_length=1000, null=True, blank=True)
    education = models.CharField('education', max_length=1000, null=True, blank=True)
    experience = models.CharField('experience', max_length=1000, null=True, blank=True)
    experience_json = models.CharField('experience_json', max_length=1000, null=True, blank=True)
    hobbies = models.CharField('hobbies', max_length=1000, null=True, blank=True)
    interest = models.CharField('interest', max_length=1000, null=True, blank=True)
    language = models.CharField('language', max_length=1000, null=True, blank=True)
    objective = models.CharField('objective', max_length=1000, null=True, blank=True)
    personal_details = models.CharField('personal_detials', max_length=1000, null=True, blank=True)
    personal_details_json = models.CharField('personal_detials_json', max_length=1000, null=True, blank=True)
    reference = models.CharField('reference', max_length=1000, null=True, blank=True)
    seminar = models.CharField('seminar', max_length=1000, null=True, blank=True)
    soft_skill = models.CharField('soft_skill', max_length=1000, null=True, blank=True)
    technical_skill = models.CharField('technical_skill', max_length=1000, null=True, blank=True)
    technical_skill_json = models.CharField('technical_skill_json', max_length=1000, null=True, blank=True)
    iv = models.CharField('iv', max_length=1000, null=True, blank=True)
    project = models.CharField('project', max_length=1000, null=True, blank=True)
    project_json = models.CharField('project_json', max_length=1000, null=True, blank=True)
    training = models.CharField('training', max_length=1000, null=True, blank=True)
    last_uploaded_on = models.DateTimeField('Uploaded On', auto_now_add=True)

    def __str__(self):
        return self.user.username



class Department(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # rules = models.ManyToManyField(Rule, through='TakenRule')
    rules = models.ManyToManyField(Rule, related_name='resumes_rules')

    def __str__(self):
        return self.user.username




# delete the resume files associated with each object or record
@receiver(post_delete, sender=Resume)
def submission_delete(sender, instance, **kwargs):
    instance.resume.delete(False)
