from django.db import models


class Music(models.Model):
    rank = models.IntegerField()
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)

    class Meta:
        db_table = 'music'
