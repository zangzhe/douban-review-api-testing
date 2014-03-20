# -*- coding: utf-8 -*-

from .base import DoubanAPIBase
from .base import DoubanAPIBase_v1

class Review(DoubanAPIBase):

    def __init__(self, access_token, target):
        self.access_token = access_token
        self.target = target

    def new(self, target_id, title, content, rating=''):
        data = {self.target: target_id,
                'title': title,
                'content': content,
                'rating': rating, }
        return self._post('/v2/%s/reviews' % self.target, **data)

    def update(self, id, title, content, rating=''):
        data = {self.target: id,
                'title': title,
                'content': content,
                'rating': rating, }
        return self._put('/v2/%s/review/%s' % (self.target, id), **data)

    def delete(self, id):
        return self._delete('/v2/%s/review/%s' % (self.target, id))

class Review_v1(DoubanAPIBase_v1):
    def __repr__(self):
        return '<DoubanAPI Review_v1>'

    def get(self, review_id):
        return self._get('/review/%s?alt=json' % review_id)