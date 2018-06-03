import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

CHOICES = [('QA', 'QA'), ('DEV', 'DEV'), ('BA', 'BA'), ('HR', 'HR')]
STATUS = [('First', 'First'), ('Rejected', 'Rejected'), ('Next', 'Next'), ('Accepted', 'Accepted')]


class RolesForUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role = models.TextField(choices=CHOICES)

    class Meta:
        permissions = (
            ("can_access_hr", "Can Access the HR portal"),
        )


@receiver(post_save, sender=User)
def create_roles_for_user(sender, instance, created, **kwargs):
    if created:
        RolesForUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_roles_for_user(sender, instance, **kwargs):
    instance.rolesforuser.save()


class Candidate(models.Model):
    date_time = models.DateTimeField(default=datetime.datetime.now())
    created_date = models.DateField(default=datetime.date.today())
    name = models.CharField(blank=False, null=False, max_length=100)
    experience = models.IntegerField(blank=False, null=False)
    interview_date = models.DateTimeField(null=False, blank=False)
    interviewed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interviewed_by', blank=True,
                                       null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='added_by', blank=True, null=True)
    status = models.TextField(choices=STATUS, default='First')

    def __str__(self):
        return self.name
