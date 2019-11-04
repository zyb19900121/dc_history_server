from django.db import models

# Create your models here.


class Dynasty(models.Model):
    dynasty_name = models.CharField(max_length=32)
    dynasty_desc = models.CharField(null=True, max_length=255)
    dynasty_king = models.CharField(null=True, max_length=32)
    dynasty_start_time = models.CharField(null=True, max_length=32)
    dynasty_end_time = models.CharField(null=True, max_length=32)
    dynasty_order = models.IntegerField(default=1)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # 元类 用于数据排序
    class Meta:
        ordering: ("dynaset_order")
        
