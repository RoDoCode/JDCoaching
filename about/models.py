from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)
    about_image = models.URLField(max_length=1024, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content_1 = models.TextField(null=True, blank=True)
    content_2 = models.TextField(null=True, blank=True)
    content_3 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Resource(models.Model):
    title = models.CharField(max_length=200)
    name_1 = models.CharField(max_length=200, null=True, blank=True)
    url_1 = models.URLField(max_length=1024, null=True, blank=True)
    name_2 = models.CharField(max_length=200, null=True, blank=True)
    url_2 = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.title
