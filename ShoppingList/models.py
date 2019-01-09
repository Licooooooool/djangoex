from django.db import models

# Create your models here.
class MyCars(models.Model):
    ProductID = models.CharField('订单号',max_length=18)
    ProductName = models.CharField('内容',max_length=30)
    ProductPrice = models.PositiveIntegerField('价格')
    table_num = models.IntegerField('桌号',default=0)
    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'
    def __str__(self):
        return self.ProductID