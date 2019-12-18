#!/usr/bin/python                                                                  
# -*-encoding=utf8 -*-                                                             
# @Author         : imooc
# @Email          : imooc@foxmail.com
# @Created at     : 2019/1/13
# @Filename       : example.py
# @Desc           :

from django.db import models


class Wife(models.Model):
    pass

class Husband(models.Model):
    wife = models.OneToOneField(Wife, on_delete=models.CASCADE)
    pass


class Mother(models.Model):
    pass

class Father(models.Model):
    wife = models.OneToOneField(Mother, on_delete=models.DO_NOTHING)
    pass

class YoungerBrother(models.Model):
    pass

class ElderBrother(models.Model):
    father_id = models.ForeignKey(Father, on_delete=models.DO_NOTHING)
    younger_brother = models.ManyToManyField(YoungerBrother)
    pass
