from django.db import models


class log(models.Model):
    worker_id = models.IntegerField(primary_key=True)
    wlogin = models.CharField(max_length=50)
    kod = models.CharField(max_length=80)
    wname = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    USERNAME_FIELD = 'wlogin'
    class Meta:
        db_table = "workers_table"