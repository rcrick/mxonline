# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class EmailVerifyRecordAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['code', 'email', 'type', 'send_time']
    # 自定义搜索字段
    search_fields = ['code', 'email', 'type']
    # 自定义筛选字段
    list_filter = ['code', 'email', 'type', 'send_time']


class BannerAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    # 自定义搜索字段
    search_fields = ['title', 'image', 'url', 'index']
    # 自定义筛选字段
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# 注册邮件验证码
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
# 注册轮播图
xadmin.site.register(Banner, BannerAdmin)
# xadmin全局配置
xadmin.site.register(views.BaseAdminView, BaseSetting)