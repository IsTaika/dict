from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a name for a certain category of words (opt.).', null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('categories_detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Dict(models.Model):
    eng_word = models.CharField(max_length=100, help_text='Enter english word here.')
    transcript = models.CharField(max_length=150, null=True, blank=True, help_text='Enter transcription of word here '
                                                                                   '(optional).')
    rus_word = models.CharField(max_length=200, help_text='Enter russian translate.')
    exemp = models.TextField(null=True, blank=True, help_text='Enter examples for word (opt.).')
    category = models.ManyToManyField(Category, help_text='Select a category')
    executor = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.eng_word

    def get_absolute_url(self):
        return reverse('word-detail', args=[str(self.id)])






