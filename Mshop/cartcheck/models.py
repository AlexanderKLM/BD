from django.db import models
from djmoney.models.fields import MoneyField

class Orderlist(models.Model):
    check_id = models.IntegerField(primary_key=True)
    total_cost = models.IntegerField
    odate = models.DateTimeField
    ostatus = models.CharField(max_length=50)
    user_id = models.IntegerField(primary_key=False)
    catalog_id = models.IntegerField(primary_key=False)
    delivery_id = models.IntegerField(primary_key=False)
    class Meta:
        db_table = "cart"