# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
from course.models import Course


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"姓名")
    mobile = models.IntegerField(max_length=11, verbose_name=u"手机号")
    course_name = models.CharField(max_length=50, verbose_name=u"课程名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    "课程评论"
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    comments = models.CharField(max_length=200, verbose_name=u"课程评论")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"评论时间")

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    choices = (
        (1, u"课程"),
        (2, u"课程机构"),
        (3, u"讲师")
    )
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
    fav_type = models.IntegerField(choices=choices, default=1, verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"收藏时间")

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    # user == 0: 给所用用户发消息
    user = models.IntegerField(default=0, verbose_name=u'接收用户')
    message = models.CharField(max_length=500, verbose_name=u'消息内容')
    has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间")

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")
    course = models.ForeignKey(Course, verbose_name=u"课程")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"学习时间")

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name
