# -*- coding: utf-8 -*-
import xadmin

from models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    # 自定义搜索字段
    search_fields = ['name', 'mobile', 'course_name']
    # 自定义筛选字段
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentsAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['user', 'course', 'comments', 'add_time']
    # 自定义搜索字段
    search_fields = ['user', 'course', 'comments']
    # 自定义筛选字段
    list_filter = ['user__nick_name', 'course__name', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    # 自定义搜索字段
    search_fields = ['user', 'fav_id', 'fav_type']
    # 自定义筛选字段
    list_filter = ['user__nick_name', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['user', 'message', 'has_read', 'add_time']
    # 自定义搜索字段
    search_fields = ['user', 'message', 'has_read']
    # 自定义筛选字段
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['user', 'course', 'add_time']
    # 自定义搜索字段
    search_fields = ['user', 'course']
    # 自定义筛选字段
    list_filter = ['user__nick_name', 'course__name', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
