from django.db import models

# Create your models here.
class ProductDetail (models.Model):
    ProductID = models.CharField('菜品编号',max_length=18)
    ProductName = models.CharField('菜名',max_length=30)
    ProductPrice = models.PositiveIntegerField('价格')
    ProductNumber= models.CharField('规格',max_length=30)
    ProductOffer = models.CharField('其他',max_length=30)
    class Meta:
        verbose_name = '菜品'
        verbose_name_plural = '菜品信息'
    def __str__(self):
         return self.ProductID