from django.db import models

class Stock(models.Model):
    name = models.CharField(max_length=100, verbose_name="商品名")
    quantity = models.PositiveIntegerField(verbose_name="在庫数")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="価格")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    def __str__(self):
        return self.name