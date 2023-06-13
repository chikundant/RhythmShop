from django.db import models
from django.urls import reverse


class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    price = models.IntegerField()
    description = models.TextField()
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    category = models.ForeignKey('CategoryModel', on_delete=models.PROTECT)
    manufacturer = models.CharField(max_length=75)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('overview', kwargs={'slug': self.slug})


class CategoryModel(models.Model):
    title = models.CharField(max_length=140, null=False)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title
