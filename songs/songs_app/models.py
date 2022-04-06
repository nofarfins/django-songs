from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256)
    age = models.PositiveIntegerField(null=False, blank=False)
    information = models.CharField(null=False, blank=False, max_length=4256)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(null=False, blank=False, max_length=256)
    lyrics = models.CharField(null=False, blank=False, max_length=4256)
    song_writer = models.ForeignKey(to=Artist, on_delete=models.RESTRICT, related_name='writer')
    song_composer = models.ForeignKey(to=Artist, on_delete=models.RESTRICT, related_name='composer')
    performed_by = models.ManyToManyField(to=Artist, through="Performance")

    def __str__(self):
        return self.name


class Performance(models.Model):
    song = models.ForeignKey(to=Song, on_delete=models.RESTRICT)
    singer = models.ForeignKey(to=Artist, on_delete=models.RESTRICT)
    Amount_of_views= models.PositiveIntegerField(null=False, blank=False)
    link = models.URLField(max_length=512, null=True, blank=True)



class Review(models.Model):
    Performance_id = models.ForeignKey(to=Performance, on_delete=models.RESTRICT, null=False, blank=False)
    review_title = models.CharField(null=False, blank=False, max_length=128)
    review_text = models.CharField(null=False, blank=False, max_length=512)
    user = models.ForeignKey(to=User, on_delete=models.RESTRICT, null=False, blank=False)





