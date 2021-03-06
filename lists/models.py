from django.db import models
from django.shortcuts import reverse

class List(models.Model):
    def get_absolute_url(self):
        return reverse('lists:view_list', args=[self.id])


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('list', 'text')