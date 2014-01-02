from django.db import models


class Talk(models.Model):

    title = models.CharField(max_length=255)

    approved = models.NullBooleanField()
    recording_release = models.BooleanField(default=False)

    outline = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(str(self))
