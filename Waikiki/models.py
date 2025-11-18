from django.db import models

class Caterory_Clothes(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='Описание товара')
    tags = models.ManyToManyField(Caterory_Clothes)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}-{", ".join(i.name for i in self.tags.all() )}'
