from django.db import models
# Create your models here.


class NewsBbc(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    place = models.CharField(max_length=20)
    date = models.DateField()
    content = models.TextField()

    def __unicode__(self):  # unicode make code is more readable
        return self.title



