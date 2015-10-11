#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django_cache.common.base_dao import BaseDao
from django_cache.people.model import People

__author__ = 'Zhangxiaofan'


class PeopleDao(BaseDao):

    def __init__(self):
        # python2.x中的继承方式如下 python3.0中为super().__init__(xxx)
        BaseDao.__init__(self, People)

    def people_add(self, name, age):
        people = People()
        people.name = name
        people.age = age
        people = self.cache_add(people)
        print u"插入成功，People:" + str(people.id)
        return people

    def people_get(self, people_id):
        people = self.cache_get(people_id)
        print u'获取对象成功：' + people.name
        return people

    def people_delete(self, people_id):
        people = self.cache_delete(people_id)
        print u'删除对象成功：' + people.name

    def people_update(self, people_id, update_dict):
        people = self.cache_update(people_id, update_dict)
        print u'更新对象成功：' + people.name

    def people_select(self, name, age):
        peoples = self.model_select("name like %s and age = %s", [name, age])
        print u'查询对象成功--------------'
        for people in peoples:
            print u'people-->' + people.name
        return peoples

    def people_select_age(self, age):
        peoples = self.model_select("age = %s", age)
        print u'查询对象成功--------------'
        for people in peoples:
            print u'people-->' + people.name
        return peoples
