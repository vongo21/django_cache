#!/usr/bin/env python
# -*- coding:utf-8 -*-
from config import MEMCACHED_SERVERS
from config import MEMCACHED_DEBUG
import memcache

__author__ = 'Zhangxiaofan'


class MemcachedClient(object):
    """
    MC缓存操作类
    """

    def __init__(self):
        self.client = memcache.Client(MEMCACHED_SERVERS, MEMCACHED_DEBUG)

    def set(self, key, value, expired=0):
        """
        设值，key重复时覆盖
        :param key: 键
        :param value: 值
        :param expired: 过期时间
        :return:
        """
        self.client.set(key, value, expired)

    def get(self, key):
        """
        根据指定key获值
        :param key: 键
        :return:
        """
        return self.client.get(key)

    def delete(self, key):
        """
        删除指定键对应缓存
        :param key:
        :return:
        """
        self.client.delete(key)

    def set_multi(self, key_value_maps, key_prefix='', time=0):
        """
        一次性设置多个键值对
        :param key_value_maps: key-value字典对象
        :param key_prefix: 键的前缀
        :param time:    缓存有效时间
        :return:
        """
        self.client.set_multi(key_value_maps, time, key_prefix)

    def get_multi(self, keys, key_prefix=''):
        """
        一次性获取多个键值
        :param keys: 键数组对象
        :param key_prefix: 键前缀
        :return: key-value字典
        """
        return self.client.get_multi(keys, key_prefix)

    def delete_multi(self, keys, key_prefix='', time=0):
        """
        一次性删除多个键
        :param keys: 键数组对象
        :param key_prefix: 键前缀
        :param time:
        :return:
        """
        self.client.delete_multi(keys, time, key_prefix)

    def append_value(self, key, value, time=0):
        """
        在指定键的值后面追加value
        :param key:  键
        :param value: 追加的值
        :param time: 缓存时间
        :return:
        """
        self.client.append(key, value, time)

    def prepend_value(self, key, value, time=0):
        """
        在指定的键前面追加value
        :param key:  键
        :param value: 追加的值
        :param time: 缓存时间
        :return:
        """
        self.client.prepend(key, value, time)

    def incr_value(self, key, delta=1):
        """
        原子增加指定键的值
        :param key: 键
        :param delta: 增加步长
        :return: 改变后的值
        """
        return self.client.incr(key, delta)

    def decr_value(self, key, delta=1):
        """
        原子减少指定键的值
        :param key: 键
        :param delta: 减少步长
        :return: 改变后的值
        """
        return self.client.decr(key, delta)


if __name__ == '__main__':
    print '---------'