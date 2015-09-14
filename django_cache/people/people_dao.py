#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django_cache.common.base_dao import BaseDao
from django_cache.people.model import People

__author__ = 'Administrator'


class PeopleDao(BaseDao):

    def __init__(self):
        # python2.x中的继承方式如下 python3.0中为super().__init__(xxx)
        BaseDao.__init__(self, People)

