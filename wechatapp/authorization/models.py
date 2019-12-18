from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    # open_id
    open_id = models.CharField(max_length=64, unique=True)
    # 昵称
    nickname = models.CharField(max_length=256)
    # 关注的城市
    focus_cities = models.TextField(default='[]')
    # 关注的星座
    focus_constellations = models.TextField(default='[]')
    # 关注的股票
    focus_stocks = models.TextField(default='[]')

    class Meta:
        indexes = [
            models.Index(fields=['nickname']),
            models.Index(fields=['open_id', 'nickname'])
        ]

    def __str__(self):
        return '%s' % (self.nickname)