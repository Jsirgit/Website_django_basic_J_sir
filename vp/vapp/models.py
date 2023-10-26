from django.db import models


class Member(models.Model):
    # id = models.CharField(max_length=10, primary_key=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    country = models.CharField(max_length=50, null=True)
    subject = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.fname
