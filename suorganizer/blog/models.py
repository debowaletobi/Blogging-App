from django.db import models
from organizer.models import Startup, Tag

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=63,
                            help_text=' A label for URL config',
                            unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField('date published',
                                auto_now_add=True)
    tags = models.ManyToManyField(Tag,
                                  related_name='blog_posts')
    startup = models.ManyToManyField(Startup,
                                     related_name='blog_posts')

    def __str__(self):
        return f'{self.title} on {self.pub_date.strftime('%Y-%m-%d')}'