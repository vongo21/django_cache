#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'Zhangxiaofan'

from mc_util import MemcachedClient
from django_cache.cache.json_util import *
import functools

memcached_client = MemcachedClient()


def cache_set(expired=0):
    """
    缓存设值装饰器函数
    :param expired: 缓存时间
    :return:
    """
    def set_func(func):
        @functools.wraps(func)
        def cache_func(*args, **kwargs):
            # 将原本函数要返回的值取出，插入缓存中
            entity = func(*args, **kwargs)
            if entity:
                object_name = entity._meta.model_name
                key = object_name + '_' + str(entity.id)
                value = object_to_json(entity)
                memcached_client.set(key, value, expired)
            return entity
        print '# 将原本函数要返回的值取出，插入缓存中'
        return cache_func
    return set_func


def cache_get():
    """
    缓存取值装饰器函数
    :param cache: 是否缓存
    :return:
    """
    def get_func(func):
        @functools.wraps(func)
        def cache_func(*args, **kwargs):
            # 根据函数的处理条件，先查询缓存中是否存在，不存在则查询函数，并将其设置进缓存中,返回
            cls_obj = args[0].model
            key = cls_obj._meta.model_name + '_' + str(args[1])
            value = memcached_client.get(key)
            if value:
                value = json_to_object(cls_obj, value)
            else:
                value = func(*args, **kwargs)
                if value:
                    memcached_client.set(key, object_to_json(value))
            return value
        print '# 根据函数的处理条件，先查询缓存中是否存在，不存在则查询函数，并将其设置进缓存中,返回'
        return cache_func
    return get_func


def cache_update(expired=0):
    """
    缓存更新装饰器函数
    :param cls_obj: models.Model子类
    :param expired: 缓存时间
    :return:
    """
    def update_func(func):
        @functools.wraps(func)
        def cache_func(*args, **kwargs):
            # 根据函数的更新结果，相应更新缓存中的值
            value = func(*args, **kwargs)
            if value:
                cls_obj = args[0].model
                key = cls_obj._meta.model_name + '_' + str(args[1])
                memcached_client.set(key, object_to_json(value), expired)
            return value
        print '# 根据函数的更新结果，相应更新缓存中的值'
        return cache_func
    return update_func


def cache_delete():
    """
    缓存删除装饰器函数
    :param cls_obj: models.Model子类
    :return:
    """
    def delete_func(func):
        @functools.wraps(func)
        def cache_func(*args, **kwargs):
            # 根据函数处理条件，优先删除缓存，并删除对应数据库记录
            value = func(*args, **kwargs)
            if value:
                cls_obj = args[0].model
                key = cls_obj._meta.model_name + '_' + str(args[1])
                memcached_client.delete(key)
            return value

        print '# 根据函数处理条件，优先删除缓存，并删除对应数据库记录'
        return cache_func
    return delete_func

