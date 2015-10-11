#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django_cache.cache.cache_decorator import *

__author__ = 'Zhangxiaofan'


class BaseDao(object):
    def __init__(self, model):
        self.model = model

    @cache_set()
    def cache_add(self, model):
        """
        插入缓存中
        :param model:
        :return:
        """
        return self.db_add(model)

    def db_add(self, model):
        """
        数据库保存记录
        :param model:
        :return:
        """
        if isinstance(model, self.model):
            model.save()
            return model
        else:
            raise TypeError('传入的model对象不是models.Model类型的！')
        return None

    @cache_get()
    def cache_get(self, model_id):
        return self.db_get(model_id)

    def db_get(self, model_id):
        model_list = self.model.objects.filter(id=model_id).all()
        if len(model_list) > 0:
            return model_list[0]
        return None

    @cache_update()
    def cache_update(self, model_id, update_dict):
        """
        数据库更新、缓存更新
        :param model_id:
        :param update_dict:
        :return:
        """
        return self.db_update(model_id, update_dict)

    def db_update(self, model_id, update_dict):
        """
        更新数据库
        :param model_id:
        :param update_dict:
        :return:
        """
        if update_dict and isinstance(update_dict, dict):
            model = self.db_get(model_id)
            if model:
                for column, value in update_dict.items():
                    if hasattr(model, column):
                        setattr(model, column, value)
                model.save()
            return model
        return None

    @cache_delete()
    def cache_delete(self, model_id):
        return self.db_delete(model_id)

    def db_delete(self, model_id):
        """
        数据库删除指定id记录
        :param model_id:
        :return:
        """
        model = self.db_get(model_id)
        if model:
            model.delete()
        return model

    def model_select(self, where, args):
        table_name = self.model._meta.app_label + '_' + self.model._meta.model_name
        args_list = list()
        if isinstance(args, list):
            for arg in args:
                args_list.append(arg)
        else:
            args_list.append(args)
        sql = 'select id from %s where ' % table_name + where
        model_list = list()
        id_rows = self.model.objects.raw(sql, args_list)
        if id_rows:
            for id_row in id_rows:
                model = self.cache_get(id_row.id)
                model_list.append(model)
        return model_list
