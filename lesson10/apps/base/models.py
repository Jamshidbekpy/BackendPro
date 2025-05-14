from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True



class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="Country name")
    code = models.CharField(max_length=2, verbose_name="Country code")
    is_active = models.BooleanField(default=True)
    img = models.ImageField(upload_to="countries/", blank=True, null=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name