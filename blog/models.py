# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 指向另一个模型的连接
    title = models.CharField(max_length=200) # 长度有限字符文本
    text = models.TextField() # 无长度限制长文本
    created_date = models.DateTimeField( # 日期和时间
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title