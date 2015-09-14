#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django_cache.cache.cache_decorator import *

__author__ = 'Administrator'


class BaseDao(object):

    def __init__(self, model):
        print 'init father...........'
        self.model = model

    @cache_set()
    def model_add(self, model):
        if isinstance(model, models.Model):
            model.save()
            return model
        else:
            raise TypeError('传入的model对象不是models.Model类型的！')
        return None

    @cache_get()
    def model_get(self, model_id):
        return self._get(model_id)

    def _get(self, model_id):
        model_list = self.model.objects.filter(id=model_id).all()
        if len(model_list) > 0:
            return model_list[0]
        return None

    @cache_update()
    def model_update(self, model_id, update_dict):
        if update_dict and isinstance(update_dict, dict):
            model = self.model_get(model_id)
            if model:
                for column, value in update_dict.items():
                    if hasattr(model, column):
                        setattr(model, column, value)
                model.save()
            return model
        return None

    @cache_delete()
    def model_delete(self, model_id):
        model = self._get(model_id)
        if model:
            model.delete()
        return model

    def model_select(self, where, args):
        table_name = self.model._meta.app_label + '_' + self.model._meta.model_name
        args_tuple = tuple()
        args_tuple.__add__(table_name)
        if isinstance(args, tuple):
            for arg in args:
                args_tuple.__add__(arg)
        else:
            args_tuple.__add__(args)
        sql = 'select id from %s where ' + where % args_tuple
        model_list = list()
        id_rows = self.model.objects.raw(sql)
        if not id_rows:
            for id_row in id_rows:
                model = self.model_get(id_row.id)
                model_list.append(model)
