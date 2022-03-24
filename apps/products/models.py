from django.db import models

from apps.categories.models import Category


class Product(models.Model):

    title = models.CharField(
        max_length=255
    )
    description = models.TextField()
    price = models.PositiveIntegerField(
        default=0
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='product_category'
    )
    image = models.ImageField(
        upload_to='product_images'
    )

    def __str__(self):
        return self.title
