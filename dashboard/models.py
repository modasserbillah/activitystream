#dashboard.models
from django.db import models
from django.contrib.auth.models import User
from actstream import action

# Create your models here.


class Employee(models.Model):
    user = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    created_by = models.CharField(max_length=200, null=True, editable=False)
    modified_by = models.CharField(max_length=200, null=True, blank=True)

    def __unicode__(self):
        return self.user

    def save(self, *args, **kwargs):

        super(Employee, self).save(*args, **kwargs) # Call the "real" save() method.
        action.send(self.created_by, verb='added a new employee', target=self)

    
