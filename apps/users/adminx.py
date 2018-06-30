# -*- coding: utf-8 -*-
import xadmin

from models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['code', 'email', 'type', 'send_time']
    # 自定义搜索字段
    search_fields = ['code', 'email', 'type']
    # 自定义筛选字段
    list_filter = ['code', 'email', 'type', 'send_time']


# 注册邮件验证码
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
