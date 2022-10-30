from django.db import models

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=255)
    Last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    title = models.CharField(max_length=50)
    date_released = models.DateField()
    likes = models.IntegerField(default=0)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.PROTECT)

    def __str__(self):
        return self.content



