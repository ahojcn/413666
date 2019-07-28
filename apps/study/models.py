from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    """用户基类"""

    avatar = models.CharField(max_length=256, verbose_name='头像')
    comment = models.CharField(max_length=256, verbose_name='个性签名')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        db_table = 'ss_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class StudyRecord(models.Model):
    """学习记录类"""

    user = models.ForeignKey('User', verbose_name='记录所属用户', on_delete=None)
    start_time = models.DateTimeField(verbose_name='开始学习时间')
    end_time = models.DateTimeField(verbose_name='结束学习时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
