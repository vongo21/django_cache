#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.db import connection
from django_cache.people.model import People
from django_cache.people.people_dao import PeopleDao

__author__ = 'Administrator'

from django_cache.cache.cache_decorator import *


@cache_set()
def people_add(name, age):
    people = People()
    people.name = name
    people.age = age
    people.save()
    return people


@cache_get()
def people_get(people_id):
    print 'people_get'
    return _get(people_id)


@cache_update()
def people_update(people_id, name):
    people = people_get(people_id)
    if people:
        people.name = name
        people.save()
    print 'people_update'
    return people


@cache_delete()
def people_delete(people_id):
    people = _get(people_id)
    if people:
        people.delete()
    print 'people_delete'
    return people


def _get(people_id):
    peoples = People.objects.filter(id=people_id).all()
    if len(peoples) > 0:
        return peoples[0]
    return None


def people_select(age):
    print 'people_select'
    sql = 'select id from people where age = %s' % age
    cursor = connection.cursor()
    cursor.execute(sql)
    ids = cursor.fetchall()
    peoples = list()
    for people_id in ids:
        people = people_get(people_id[0])
        peoples.append(people)
    return peoples

if __name__ == '__main__':
    people_add('zhangxiaofan', 24)
    peopleDao = PeopleDao()

