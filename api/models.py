from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# uuid
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.TextField()

    def __str__(self) -> str:
        return self.name


class Rater(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    starts = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.product)

    class Meta:
        unique_together = (('user', 'product'),)
        index_together = (('user', 'product'),)
