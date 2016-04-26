#!/usr/bin/python
# vim: set fileencoding=utf-8 :

from django.db import models
from wechat_member.models import Member as WxMember

class Address(models.Model):
    member = models.ForeignKey(WxMember, related_name='addresses',\
                               verbose_name='会员')
    name = models.CharField(max_length=200, verbose_name='姓名')
    mobile = models.CharField(max_length=20, verbose_name='手机号码')
    location = models.CharField(max_length=200, verbose_name='名称')
    address = models.CharField(max_length=200, verbose_name='详细地址')
    longitude = models.DecimalField(max_digits=14, decimal_places=10, \
                                    verbose_name='经度')
    latitude = models.DecimalField(max_digits=13, decimal_places=10, \
                                   verbose_name='维度')
    created = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    class Meta(object):
        verbose_name = '地址'
        verbose_name_plural = '地址'
