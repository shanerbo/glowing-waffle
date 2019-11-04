from django.db import models
from datetime import datetime

default_category_url = "https://storage.googleapis.com/mysite-cardview-img/categories_default_img.jpeg"
default_series_url = "https://storage.googleapis.com/mysite-cardview-img/series_default_img.jpeg"
default_new_url = "https://storage.googleapis.com/mysite-cardview-img/new_default_img.jpeg"

# Create your models here.
class NewCategory(models.Model):
    new_category = models.CharField(max_length=200)
    category_summary = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200, default=1)
    category_url = models.CharField(max_length=200, default=default_category_url)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.new_category


class NewSeries(models.Model):
    new_series = models.CharField(max_length=200)
    new_category = models.ForeignKey(NewCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    series_summary = models.CharField(max_length=200)
    series_url = models.CharField(max_length=200, default=default_series_url)


    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.new_series


class New(models.Model):
    new_title = models.CharField(max_length=200)
    new_content = models.TextField()
    new_publish = models.DateTimeField("date published", default=datetime.now())

    new_series = models.ForeignKey(NewSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)

    new_slug = models.CharField(max_length=200, default=1)

    new_url = models.CharField(max_length=200, default=default_new_url)

    def __str__(self):
        return self.new_title
