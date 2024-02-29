from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.


class AbstractBaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(AbstractBaseModel, AbstractBaseUser):
    username = models.CharField(max_length=56, unique=True)
    first_name = models.CharField(max_length=56)
    last_name = models.CharField(max_length=56)
    avatar = models.ImageField(upload_to="authors/avatar/%Y/%m/%d", default='media/author_avatar.jpg')
    like_count = models.IntegerField(default=0)
    product = models.ManyToManyField("Product", related_name="authors")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        db_table = "authors"


class Product(AbstractBaseModel):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="products/avatar/%Y/%m/%d", default='media/product_avatar.jpg')
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="products")
    description = models.TextField()
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.CharField(max_length=56)
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "products"

