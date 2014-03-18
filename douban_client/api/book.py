# -*- coding: utf-8 -*-

from .subject import Subject
from .base import DoubanAPIBase_v1

class Book(Subject):

    target = 'book'

    def __repr__(self):
        return '<DoubanAPI Book>'

    def isbn(self, isbn_id):
        return self._get('/v2/book/isbn/%s' % isbn_id)


class Book_v1(DoubanAPIBase_v1):

    def __repr__(self):
        return '<DoubanAPI Book_v1>'

    def reviews(self, book_id = '', start_index = '', max_results = '', orderby = ''):
        return self._get('/book/subject/%s/reviews?alt=json&start-index=%s&max-results=%s&orderby=%s' % (book_id, start_index, max_results, orderby))
        
    def reviews_isbn(self, isbn_id = '', start_index = '', max_results = '', orderby = ''):
        return self._get('/book/subject/isbn/%s/reviews?alt=json&start-index=%s&max-results=%s&orderby=%s' % (isbn_id, start_index, max_results, orderby))