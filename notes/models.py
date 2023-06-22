from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='audio/', blank=True, null=True)
    video = models.FileField(upload_to='video/', blank=True, null=True)

    def __str__(self):
        return self.title   
    

class SharedNote(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)