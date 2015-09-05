#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from django.http import HttpResponse
from django_cache.people.dao import *
from django_cache.utils.json_util import *

__author__ = 'Administrator'


def add_people(request):
    print 'enter add people view method....'
    name = request.GET.get('name', '')
    age = request.GET.get('age', 1)
    people_add(name, age)
    response_data = {'result': 'failed', 'message': 'You messed up'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def get_people(request):
    print 'enter get people view method....'
    people_id = request.GET.get('people_id', 1)
    people = people_get(people_id)
    print people
    data = people.to_json()
    people0 = People()
    people0.to_object(json.dumps(data))
    print people0
    response_data = {'success': True, 'data': data}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def update_people(request):
    print 'enter update people view method....'
    people_id = request.GET.get('people_id', 0)
    name = request.GET.get('name', '')
    success = True
    msg = u'更新成功'
    if people_id <= 0:
        success = False
        msg = u'id不合法'
    else:
        people_update(people_id, name)
    response_data = {'success': success, 'msg': msg}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def delete_people(request):
    print 'enter delete people view method....'
    people_id = request.GET.get('people_id', 0)
    success = True
    msg = u'删除成功'
    if people_id <= 0:
        success = False
        msg = u'id不合法'
    else:
        people_delete(people_id)
    response_data = {'success': success, 'msg': msg}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def select_people(request):
    print 'enter select people view method....'
    age = request.GET.get('age', 0)
    success = True
    msg = u'获取成功'
    datas = list()
    if age <= 0:
        success = False
        msg = u'age不合法'
    else:
        peoples = people_select(age)
        if peoples:
            for people in peoples:
                datas.append(people.to_json())
    response_data = {'success': success, 'msg': msg, 'datas': datas}
    return HttpResponse(json.dumps(response_data), content_type="application/json")