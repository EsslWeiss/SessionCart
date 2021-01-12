from django.db import models
from django.utils import timezone

from django.urls import reverse


class Category(models.Model):
    """
        Category model.
    """
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    class Meta:
        index_together = (('name', 'slug'), )

    def get_absolute_url(self):
        return reverse('CategoryDetailView', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):
    """
        Product model.
    """
    class Meta:
        ordering = ('createdAt', 'updatedAt')
        index_together = (('id', 'slug'), )

    category = models.ManyToManyField(
        Category,
        related_name='product_related',
        related_query_name='product_query_related'
    )

    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField()
    slug = models.SlugField(max_length=100, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('ProductDetailView', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

