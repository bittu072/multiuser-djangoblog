from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


def upload_path(obj, file_name):
    return "%s/%s" % (obj.id, file_name)


class Post(models.Model):
    title = models.CharField(max_length=150)
    # image = models.FileField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_path, null=True, blank=True)
    content = models.TextField()
    # auto_now=True, auto_now_add=False means everytime it get updated or edited it saves the time
    postupdate = models.DateTimeField(auto_now=True, auto_now_add=False)
    # auto_now=False, auto_now_add=True means it only saves time when it was added to the database
    posttime = models.DateTimeField(auto_now=False, auto_now_add=True)

    # For python2
    def __unicode__(self):
        return self.title

    # For python3
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:show_post", kwargs={"id": self.id})
