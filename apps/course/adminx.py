# -*- coding: utf-8 -*-
import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['name', 'descriptor', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                    'click_nums', 'add_time']
    # 自定义搜索字段
    search_fields = ['name', 'descriptor', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                     'click_nums']
    # 自定义筛选字段
    list_filter = ['name', 'descriptor', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image',
                   'click_nums', 'add_time']


class LessonAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['course', 'name', 'add_time']
    # 自定义搜索字段
    search_fields = ['course', 'name']
    # 自定义筛选字段
    list_filter = ['course__name', 'name', 'add_time']


class VideoAadmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['lesson', 'name', 'add_time']
    # 自定义搜索字段
    search_fields = ['lesson', 'name']
    # 自定义筛选字段
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['course', 'name', 'download', 'add_time']
    # 自定义搜索字段
    search_fields = ['course', 'name', 'download']
    # 自定义筛选字段
    list_filter = ['course__name', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAadmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
