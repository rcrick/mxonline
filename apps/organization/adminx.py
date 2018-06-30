# -*- coding: utf-8 -*-
import xadmin

from models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['name', 'desc', 'add_time']
    # 自定义搜索字段
    search_fields = ['name', 'desc']
    # 自定义筛选字段
    list_filter = ['name', 'desc', 'add_time']

class CourseOrgAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'add_time']
    # 自定义搜索字段
    search_fields = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city']
    # 自定义筛选字段
    list_filter = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    # 自定义xadmin端需要显示打列
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums', 'add_time']
    # 自定义搜索字段
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums']
    # 自定义筛选字段
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_num', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

