# -*- coding: utf-8 -*-
import xadmin

from models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    pass

# 注册邮件验证码
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
