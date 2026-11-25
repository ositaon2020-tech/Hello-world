from django.db import models

# Create your models here.
class PageVisit(models.Model):
    #db -> table
    path = models.TextField(blank=True, null=True) #
    timestamp = models.DateTimeField(auto_now_add=True) # auto_now_add -> timestamp will be added automatically when a new record is created

    def __str__(self):
        return self.path