# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, main, status_code, test_runner
import unittest
import pdb
import json
from time import sleep

class TestApiIdReview(DoubanClientTestBase):
    def setUp(self):
        super(TestApiIdReview, self).setUp()
        self.review_id = '1318949'
        print 'Running ' + self.id()

    # 获取特定id评论功能测试函数
    def test_get_reviews_function_v1(self):
        stat, ret = self.client_v1.review.get(self.review_id)
        ret = json.loads(ret)
        self.assertEqual(stat, status_code['OK'])
        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(self.review_id in ret['id']['$t'])
        
    # 针对 review_id 的获取特定评论异常测试函数
    def test_get_reviews_exception_review_id_v1(self):
        invalid_review_id = 'BadUserId'   # bad review id
        stat, ret = self.client_v1.review.get(invalid_review_id)
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertTrue(isinstance(ret, str))
        self.assertEqual('wrong subject id:\'' + invalid_review_id +'\'', ret)      
        
        invalid_review_id = '0000001'   # wrong review id
        stat, ret = self.client_v1.review.get(invalid_review_id)
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertTrue(isinstance(ret, str))
        self.assertEqual('wrong subject id:\'' + invalid_review_id +'\'', ret)
        
        invalid_review_id = ''   # empty review id
        stat, ret = self.client_v1.review.get(invalid_review_id)
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertTrue(isinstance(ret, str))
        self.assertEqual('wrong subject id:\'' + invalid_review_id +'\'', ret)
        
if __name__ == '__main__':
    
    main(testRunner=test_runner())
    
