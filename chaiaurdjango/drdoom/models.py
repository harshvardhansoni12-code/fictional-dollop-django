from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    USER_TYPE_CHOICE=[
        ('N', 'NORMAL'),
        ('SH', 'SUPERHERO'),
        ('CEL', 'CELESTIAL')
    ]
    name = models.CharField(max_length=100, default="unknown")
    image = models.ImageField(upload_to='drdooms/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=USER_TYPE_CHOICE)
    description=models.TextField()
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user}'        
        