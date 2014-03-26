# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, main, status_code, test_runner
import pdb
import json
from time import sleep

class TestApiMovieReview(DoubanClientTestBase):
    def setUp(self):
        super(TestApiMovieReview, self).setUp()
        self.movie_id = '11606328'
        self.start_index = '2'
        self.max_results = '4'
        self.orderby_time = 'time'
        self.orderby_score = 'score'
        self.title = self.content = uuid4().hex
        self.content = self.content * 10
        self.rating = '5'
        print 'Running ' + self.id()
    
    # 增删改电影评论功能测试函数
    def test_new_update_delete_review_function_v2(self):
        # new
        stat, ret = self.client_v2.movie.review.new(self.movie_id, \
            self.title, self.content)
        self.assertEqual(stat, status_code['CREATED'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)

        # update
        review_id = ret['id']
        content = self.content * 2
        stat, ret = self.client_v2.movie.review.update(review_id, \
            self.title, content)
        self.assertEqual(stat, status_code['ACCEPTED'])
        self.assertEqual(content, ret['content'])

        # delete
        stat, ret = self.client_v2.movie.review.delete(review_id)
        self.assertEqual(stat, status_code['OK'])
        self.assertEqual('OK', ret)

    # 针对 movie_id 的发布电影评论异常测试函数
    def test_new_review_exception_movie_id_v2(self):
        invalid_movie_id = '1000000000000' # wrong movie id
        stat, ret = self.client_v2.movie.review.new(invalid_movie_id, \
            self.title, self.content)
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('movie_not_found', ret['msg'])
        self.assertEqual(5000, ret['code'])        
        
        invalid_movie_id = 'abcdefg' # bad movie id
        stat, ret = self.client_v2.movie.review.new(invalid_movie_id, \
            self.title, self.content)
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('movie_not_found', ret['msg'])
        self.assertEqual(5000, ret['code'])       

        invalid_movie_id = '' # null movie id
        stat, ret = self.client_v2.movie.review.new(invalid_movie_id, \
            self.title, self.content)        
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertTrue(isinstance(ret, dict))
        # check str and code
        self.assertEqual('movie_not_found', ret['msg'])
        self.assertEqual(5000, ret['code'])
    
    # 针对 title 的发布电影评论异常测试函数
    def test_new_review_exception_title_v2(self): 
        invalid_title = self.title*200 # too long title
        stat, ret = self.client_v2.movie.review.new(self.movie_id, \
            invalid_title, self.content)
        self.assertEqual(stat, status_code['CREATED'])
        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(invalid_title.startswith(ret['title']))
        review_id = ret['id']
        ret = self.client_v2.movie.review.delete(review_id)
        
        invalid_title = "" # empty title
        stat, ret = self.client_v2.movie.review.new(self.movie_id, \
            invalid_title, self.content)
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('missing_args', ret['msg'])
        self.assertEqual(1002, ret['code'])
    
    # 针对 content 的发布电影评论异常测试函数
    def test_new_review_exception_content_v2(self):
        #print 'test_new_review_exception_content_v2'
        invalid_content = "TooShort" # too short content
        stat, ret = self.client_v2.movie.review.new(self.movie_id, \
            self.title, invalid_content)
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('review_content_short(should more than 150)', \
            ret['msg'])
        self.assertEqual(5004, ret['code'])         

        invalid_content = "" # empty title
        stat, ret = self.client_v2.movie.review.new(self.movie_id, \
            self.title, invalid_content)
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('review_content_short(should more than 150)', \
            ret['msg'])
        self.assertEqual(5004, ret['code'])   

    # 针对 rating 的发布电影评论异常测试函数
    def test_new_review_exception_rating_v2(self):
        invalid_rating = "BadRating" # bad rating
        stat, ret = self.client_v2.movie.review.new(self.movie_id, self.title, \
            self.content, invalid_rating)
        # attention!!!! no rating error answer
        self.assertEqual(stat, status_code['CREATED'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)
        review_id = ret['id']
        stat, ret = self.client_v2.movie.review.delete(review_id)

        invalid_rating = "-1" # too small rating
        stat, ret = self.client_v2.movie.review.new(self.movie_id, self.title, \
        self.content, invalid_rating)
        # attention!!!! no rating error answer
        self.assertEqual(stat, status_code['CREATED'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)
        review_id = ret['id']
        stat, ret = self.client_v2.movie.review.delete(review_id)
        
        invalid_rating = "6" # too big rating
        stat, ret = self.client_v2.movie.review.new(self.movie_id, self.title, \
        self.content, invalid_rating)
        # attention!!!! no rating error answer
        self.assertEqual(stat, status_code['CREATED'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)
        review_id = ret['id']
        stat, ret = self.client_v2.movie.review.delete(review_id)

    # 针对 review_id 的更新电影评论异常测试函数
    def test_update_review_exception_review_id_v2(self):  
        invalid_review_id = 'BadReviewId' # bad review id
        content = self.content * 2
        stat, ret = self.client_v2.movie.review.update(invalid_review_id, \
            self.title, content)
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('invalid_request_uri', ret['msg'])
        self.assertEqual(107, ret['code'])

        invalid_review_id = '1000000000' # wrong review id
        content = self.content * 2
        stat, ret = self.client_v2.movie.review.update(invalid_review_id, \
            self.title, content)
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('review_not_found', ret['msg'])
        self.assertEqual(5006, ret['code'])
    
    # 针对 title 的更新电影评论异常测试函数
    def test_update_review_exception_title_v2(self):
        stat, ret = self.client_v2.movie.review.new(self.movie_id, self.title, \
            self.content)
        review_id = ret['id']
        try:
            invalid_title = self.title*200 # too long title
            stat, ret = self.client_v2.movie.review.update(review_id, invalid_title,\
             self.content)    
            self.assertEqual(stat, status_code['ACCEPTED'])
            self.assertTrue(isinstance(ret, dict))
            self.assertTrue(invalid_title.startswith(ret['title']))
            invalid_title = "" # empty title
            stat, ret = self.client_v2.movie.review.update(review_id, invalid_title, \
                self.content)
            #print ret
            self.assertEqual(stat, status_code['BAD_REQUEST'])
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual('missing_args', ret['msg'])
            self.assertEqual(1002, ret['code'])
        finally:
            stat, ret = self.client_v2.movie.review.delete(review_id)
       
    # 针对 content 的更新电影评论异常测试函数  
    def test_update_review_exception_content_v2(self):
        stat, ret = self.client_v2.movie.review.new(self.movie_id, self.title,\
         self.content)
        review_id = ret['id']
        invalid_content = "TooShort" # too short content
        stat, ret = self.client_v2.movie.review.update(review_id, self.title,\
         invalid_content)    
        try:
            self.assertEqual(stat, status_code['ACCEPTED'])
            self.assertTrue(isinstance(ret, dict))
            self.assertTrue(ret.has_key('msg') and (ret['msg']==\
                'review_content_short(should more than 150)'))
        finally:
            stat, ret = self.client_v2.movie.review.delete(review_id)
    
    # 针对 rating 的更新电影评论异常测试函数
    def test_update_review_exception_rating_v2(self): 
        stat, ret = self.client_v2.movie.review.new(self.movie_id, self.title,\
         self.content)
        review_id = ret['id']

        invalid_rating = "BadRating" # bad rating
        stat, ret = self.client_v2.movie.review.update(review_id, self.title, \
            self.content, invalid_rating)
        # attention!!!! no rating error answer
        self.assertEqual(stat, status_code['ACCEPTED'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)

        invalid_rating = "-1" # too small rating
        stat, ret = self.client_v2.movie.review.update(review_id, self.title, \
            self.content, invalid_rating)
        # attention!!!! no rating error answer
        self.assertEqual(stat, status_code['ACCEPTED'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)
        
        invalid_rating = "6" # too big rating
        stat, ret = self.client_v2.movie.review.update(review_id, self.title, \
            self.content, invalid_rating)
        # attention!!!! no rating error answer
        self.assertEqual(stat, status_code['ACCEPTED'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)

        # delete
        review_id = ret['id']
        stat, ret = self.client_v2.movie.review.delete(review_id)
    
    # 针对 review_id 的删除电影评论异常测试函数
    def test_delete_review_exception_review_id_v2(self):
        invalid_review_id = "BadReviewId" # bad review id
        stat, ret = self.client_v2.movie.review.delete(invalid_review_id)
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('invalid_request_uri', ret['msg'])
        self.assertEqual(107, ret['code'])

        invalid_review_id = '1000000000' # wrong review id
        stat, ret = self.client_v2.movie.review.delete(invalid_review_id)        
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('review_not_found', ret['msg'])
        self.assertEqual(5006, ret['code'])

        invalid_review_id = '' # empty review id
        stat, ret = self.client_v2.movie.review.delete(invalid_review_id)
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('invalid_request_uri', ret['msg'])
        self.assertEqual(107, ret['code'])
    
if __name__ == '__main__':
    main(testRunner=test_runner())
