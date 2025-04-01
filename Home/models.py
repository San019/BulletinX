from django.db import models
from django.contrib.auth.models import User

class Notice(models.Model):
    CATEGORY_CHOICES = [
        ('General', 'General'),
        ('Event', 'Event'),
        ('Urgent', 'Urgent'),
        ('Academic', 'Academic'),
    ]
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='General')
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date_posted']