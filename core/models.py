from django.db import models


# Create your models here.


class Link(models.Model):
    link = models.CharField(max_length=15, primary_key=True)
    target = models.CharField(max_length=200)
    views = models.BigIntegerField(default=0, editable=False)
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link + " : " + self.target
