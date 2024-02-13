from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Categorie'

    def __str__(self) -> str:
            return self.name