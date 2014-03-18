# -*- coding: utf-8 -*-

from .base import DoubanAPIBase, DoubanAPIBase_v1, DEFAULT_START, DEFAULT_COUNT


class User(DoubanAPIBase):

    def __repr__(self):
        return '<DoubanAPI User>'

    def get(self, id):
        return self._get('/v2/user/%s' % id)

    @property
    def me(self):
        return self.get('~me')

    def search(self, q, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/user', q=q, start=start, count=count)

    def follow(self, id):
        return self._post('/shuo/v2/friendships/create', user_id=id)

    def unfollow(self, id):
        return self._post('/shuo/v2/friendships/destroy', user_id=id)

    def following(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        page = start / count
        return self._get('/shuo/v2/users/%s/following' % id, page=page, count=count)

    def followers(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        page = start / count
        return self._get('/shuo/v2/users/%s/followers' % id, page=page, count=count)

class User_v1(DoubanAPIBase_v1):

    def __repr__(self):
        return '<DoubanAPI User_v1>'

    def reviews(self, user_id = '', start_index = '', max_results = '', orderby = ''):
        return self._get('/people/%s/reviews?alt=json&start-index=%s&max-results=%s&orderby=%s' % (user_id, start_index, max_results, orderby))