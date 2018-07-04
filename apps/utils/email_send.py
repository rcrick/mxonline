# -*- coding: utf-8 -*-
from random import Random
from django.core.mail import send_mail

from MxOnline.settings import EMAIL_FROM
from users.models import EmailVerifyRecord


# 生成随机字符串
def random_str(random_length=8):
    str = ''
    # 生成字符串的可选字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


# 发送注册邮件
def send_register_email(email, type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.type = type
    email_record.save()

    email_title = ""
    email_body = ""

    if type == "register":
        email_title = u"注册激活链接"
        email_body = u"请点击下面打链接来激活帐号, http://127.0.0.1:8000/active/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif type == 'forget':
        email_title = u"密码重置链接"
        email_body = u"请点击下面打链接来重置密码, http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass