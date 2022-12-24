from django.db import models


class Shoplist(models.Model):
    catalog_id = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=50)
    category = models.CharField(max_length=80)
    cstatus = models.CharField(max_length=50)
    class Meta:
        db_table = "goodscatalog"