from django.db import models
from datetime import datetime


# Create your models here.
class NewCategory(models.Model):
    new_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.new_category


class NewSeries(models.Model):
    new_series = models.CharField(max_length=200)
    new_category = models.ForeignKey(NewCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT())


class New(models.Model):
    new_title = models.CharField(max_length=200)
    new_content = models.TextField()
    new_publish = models.DateTimeField("date published", default=datetime.now())

    def __str__(self):
        return self.new_title
