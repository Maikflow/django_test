from django.db import models

# Create your models here.
class Article(models.Model):
    """
    Title
    Body
    Date
    Likes
    """
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField()

    def __str__(self):
        return self.title



