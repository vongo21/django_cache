#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.db import models
from json import JSONDecoder
from json import JSONEncoder

__author__ = 'Administrator'


class People(models.Model):
    name = models.TextField(max_length=50, null=False)
    age = models.IntegerField(default=0)

    class Meta:
        app_label = 'people_table'
        db_table = 'people'
        verbose_name = u'人员表'

    def to_json(self):
        entity_dict = dict()
        for key, value in self.__dict__.items():
            if not key[0] == '_':
                entity_dict[key] = value
        return entity_dict

    def to_object(self, json_str):
        entity = self
        json_dict = JSONDecoder().decode(json_str)
        for key, value in json_dict.items():
            if hasattr(entity, key):
                setattr(entity, key, value)
        return entity
