from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Nomi')
    country = models.CharField(max_length=50, verbose_name='Shaxri')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Brend '
        verbose_name_plural = "Brendlar"


class Cars(models.Model):
    model = models.CharField(max_length=150, unique=True, verbose_name='modellar')
    description = models.TextField(verbose_name='Tasviri')
    year = models.IntegerField(verbose_name='Yili')
    color = models.CharField(max_length=50, verbose_name='rangi')
    price = models.IntegerField(verbose_name='Narxi')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Brendi')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Moshina'
        verbose_name_plural = 'Moshinalar'
        ordering = ['-id']
