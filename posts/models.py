from django.db import models

# Create your models here.


class Feed(models.Model):
    # id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    body = models.TextField()
    slug = models.SlugField(max_length=48)

    class Meta:
        db_table = 'posts_feed'

    def __str__(self):
        return self.title
