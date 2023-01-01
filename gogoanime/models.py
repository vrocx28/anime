from django.db import models

# Base Model
class TimeStampedModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

# Create your models here.

STATUS_CHOICES = (
    ("Complete", "Complete"),
    ("Ongoing", "Ongoing"),
    ("Upcoming", "Upcoming"),
)

class Anime_All(TimeStampedModel):
    anime_name = models.CharField(max_length=255, null=False, blank=False)
    gogoanime_url = models.CharField(max_length=255, null=False, blank=False, unique=True)
    gogoanime_id = models.IntegerField(null=False, unique=True)
    no_of_episodes = models.IntegerField(null=False)
    summary = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='anime_img/', blank=True)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES)
    # other_name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.anime_name