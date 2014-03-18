# -*- coding: utf-8 -*-

from .subject import Subject
from .base import DoubanAPIBase_v1

class Music(Subject):

    target = 'music'

    def __repr__(self):
        return '<DoubanAPI Music>'

class Music_v1(DoubanAPIBase_v1):

    def __repr__(self):
        return '<DoubanAPI Music_v1>'

    def reviews(self, music_id = '', start_index = '', max_results = '', orderby = ''):
        return self._get('/music/subject/%s/reviews?alt=json&start-index=%s&max-results=%s&orderby=%s' % (music_id, start_index, max_results, orderby))
        