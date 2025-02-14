# from django.db import models
#
# # Create your models here.
# from django.db import models
#
#
# # Create your models here.
# class Song(models.Model):
#     title = models.TextField()
#     artist = models.TextField()
#     image = models.ImageField()
#     audio_file = models.FileField(upload_to='songs/', blank=True, null=True)
#     audio_link = models.CharField(max_length=200,blank=True,null=True)
#     lyrics = models.TextField(blank=True, null=True)
#     duration = models.CharField(max_length=20)
#     paginate_by = 2
#
#     def __str__(self):
#         return self.title




from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)  # Changed to CharField
    artist = models.CharField(max_length=255)  # Changed to CharField
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Added upload_to
    audio_file = models.FileField(upload_to='songs/', blank=True, null=True)
    audio_link = models.URLField(max_length=500, blank=True, null=True)  # Changed to URLField for better link validation
    lyrics = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return self.title  # Fixed incorrect `__str__` method
