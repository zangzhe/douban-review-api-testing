# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, main                            
import pdb
import json
from time import sleep

class TestApiUserReview(DoubanClientTestBase):
    def setUp(self):
        super(TestApiUserReview, self).setUp()
        self.user_id = 'nimamui'
        self.start_index = '2'
        self.max_results = '4'
        self.orderby_time = 'time'
        self.orderby_score = 'score'
        self.title = self.content = uuid4().hex
        self.content = self.content * 10
        self.rating = '5'
        self.debug = False

    # 获取特定用户评论功能测试函数
    def test_get_reviews_function_v1(self):
        url = "/people/"+ self.user_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)

        if self.debug:
            print '## 1' 
            jdata_f = json.dumps(ret, sort_keys=True,indent=2)
            print jdata_f        
        
        self.assertTrue(isinstance(ret, dict))
        # check user_id value
        self.assertTrue(self.user_id in ret['link'][0]['@href'])
        # check start_index value
        self.assertEqual(self.start_index, ret['opensearch:startIndex']['$t'])
        # check max_results value
        self.assertEqual(self.max_results, ret['opensearch:itemsPerPage']['$t'])

    # 针对 user_id 的获取特定用户评论异常测试函数
    def test_get_reviews_exception_user_id_v1(self):
        invalid_user_id = 'BadUserId'   # bad book id
        url = "/people/"+ invalid_user_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        self.assertTrue(isinstance(ret, str))
        # check return string
        self.assertEqual('wrong people id:\'' + invalid_user_id +'\'', ret)

    # 针对 start_index 的获取特定用户评论异常测试函数
    # nimamui id has only 7 reviews
    def test_get_reviews_exception_start_index_v1(self):
        invalid_start_index = 'BadStartIndex'  # bad start index
        url = "/people/"+ self.user_id + \
        "/reviews?alt=json&start-index="+ invalid_start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)

        if self.debug:
            print '## 2'
            jdata_f = json.dumps(ret, sort_keys=True,indent=2)
            print jdata_f
        
        self.assertTrue(isinstance(ret, dict))
        # check get default max_results entries
        self.assertEqual(int(self.max_results), len(ret['entry']))
        
        invalid_start_index = '100'  # too big index entries is 0
        url = "/people/"+ self.user_id + \
        "/reviews?alt=json&start-index="+ invalid_start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)   
        self.assertTrue(isinstance(ret, dict))
        # check get 0 entry if start index too big
        self.assertEqual(0, len(ret['entry']))

        invalid_start_index = '-1'  # too small start index entries is 1
        url = "/people/"+ self.user_id + \
        "/reviews?alt=json&start-index="+ invalid_start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)      
        self.assertTrue(isinstance(ret, dict))
        # check get default max_results entries
        self.assertEqual(int(self.max_results), len(ret['entry']))
        self.assertEqual('1', ret['opensearch:startIndex']['$t'])

    # 针对 max_results 的获取特定用户评论异常测试函数
    def test_get_reviews_exception_max_results_v1(self):
        invalid_max_results = 'BadMaxResults'  # bad max results
        url = "/people/"+ self.user_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + invalid_max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)
    
        if self.debug:
            print '## 3'
            jdata_f = json.dumps(ret, sort_keys=True,indent=2)
            print jdata_f    
        
        self.assertTrue(isinstance(ret, dict))
        # check get default max_results entries
        self.assertEqual(6, len(ret['entry']))

        invalid_max_results = '51'  # too big max results > 50
        url = "/people/"+ self.user_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + invalid_max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)      
        self.assertTrue(isinstance(ret, dict))
        # check only can get 50 entries
        self.assertEqual(6, len(ret['entry']))

        invalid_max_results = '-1'  # too small max results
        url = "/people/"+ self.user_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + invalid_max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)      
        self.assertTrue(isinstance(ret, dict))
        # check get no entries
        self.assertEqual(0, len(ret['entry']))        

    # 针对 orderby 的获取特定用户评论异常测试函数
    def test_get_reviews_exception_orderby_v1(self):
        invalid_orderby = 'BadOrderBy'  # bad orderby method
        url = "/people/"+ self.user_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + invalid_orderby
        ret = self.client_v1.get(url)
        ret = json.loads(ret)
    
        if self.debug:
            print '## 4'
            jdata_f = json.dumps(ret, sort_keys=True,indent=2)
            print jdata_f

        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(int(self.max_results), len(ret['entry']))         

if __name__ == '__main__':
    main()
