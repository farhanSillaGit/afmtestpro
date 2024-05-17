from django.db import models
import datetime
class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title


