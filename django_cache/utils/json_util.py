#!/usr/bin/env python
# -*- coding:utf-8 -*-
from json import JSONDecoder
from json import JSONEncoder

__author__ = 'Administrator'


def object_to_json(entity):
    entity_dict = entity.__dict__
    return JSONEncoder().encode(entity_dict)


def json_to_object(entity_cls, json_str):
    if isinstance(entity_cls, object):
        entity = entity_cls()
        json_dict = JSONDecoder().decode(json_str)
        for key, value in json_dict.items():
            if hasattr(entity, key):
                setattr(entity, key, value)
        return entity
    print None
