# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, main, status_code, test_runner           
import pdb
import json
from time import sleep

class TestApiMusicReview(DoubanClientTestBase):
    def setUp(self):
        super(TestApiMusicReview, self).setUp()
        self.music_id = '1395762'
        #self.isbn_id = '9787020044528'
        self.start_index = '2'
        self.max_results = '4'
        self.orderby_time = 'time'
        self.orderby_score = 'score'
        self.title = self.content = uuid4().hex
        self.content = self.content * 10
        self.rating = '5'

    # 获取音乐评论功能测试函数
    def test_get_reviews_function_v1(self):
        stat, ret = self.client_v1.music.reviews(self.music_id, self.start_index,\
            self.max_results, self.orderby_score)
        ret = json.loads(ret)
        self.assertEqual(stat, status_code['OK'])
        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(self.music_id in ret['link'][0]['@href'])
        self.assertEqual(self.start_index, ret['opensearch:startIndex']['$t'])
        self.assertEqual(self.max_results, ret['opensearch:itemsPerPage']['$t'])
    
    # 增删改音乐评论功能测试函数
    def test_new_update_delete_review_function_v2(self):
        # new
        stat, ret = self.client_v2.music.review.new(self.music_id, self.title, \
            self.content)
        self.assertEqual(stat, status_code['CREATED'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)

        # update
        review_id = ret['id']
        content = self.content * 2
        stat, ret = self.client_v2.music.review.update(review_id, \
            self.title, content)
        self.assertEqual(stat, status_code['ACCEPTED'])
        self.assertEqual(content, ret['content'])

        # delete
        stat, ret = self.client_v2.music.review.delete(review_id)
        self.assertEqual(stat, status_code['OK'])
        self.assertEqual('OK', ret)
    
    # 针对 music_id 的获取音乐评论异常测试函数
    def test_get_reviews_exception_music_id_v1(self):
        invalid_music_id = 'BaiMusicId'   # bad music id
        stat, ret = self.client_v1.music.reviews(invalid_music_id, self.start_index,\
            self.max_results, self.orderby_score)
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertTrue(isinstance(ret, str))
        self.assertEqual('bad subject id', ret)

        invalid_music_id = '1000000000'   # wrong music id
        stat, ret = self.client_v1.music.reviews(invalid_music_id, self.start_index,\
            self.max_results, self.orderby_score)
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertTrue(isinstance(ret, str))
        self.assertEqual('wrong subject id', ret)

        invalid_music_id = ''   # empty music id
        stat, ret = self.client_v1.music.reviews(invalid_music_id, self.start_index,\
            self.max_results, self.orderby_score)
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertTrue(isinstance(ret, str))
        self.assertEqual('bad subject id', ret)

    # 针对 start_index 的获取音乐评论异常测试函数
    def test_get_reviews_exception_start_index_v1(self):
        invalid_start_index = 'BadStartIndex'  # bad start index
        stat, ret = self.client_v1.music.reviews(self.music_id, invalid_start_index,\
            self.max_results, self.orderby_score)
        ret = json.loads(ret)
        self.assertEqual(stat, status_code['OK'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(int(self.max_results), len(ret['entry']))
        
        invalid_start_index = '10000'  # too big index
        stat, ret = self.client_v1.music.reviews(self.music_id, invalid_start_index,\
            self.max_results, self.orderby_score)
        ret = json.loads(ret)
        self.assertEqual(stat, status_code['OK'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(0, len(ret['entry']))

        invalid_start_index = '-1'  # too small start index
        stat, ret = self.client_v1.music.reviews(self.music_id, invalid_start_index,\
            self.max_results, self.orderby_score)
        ret = json.loads(ret)
        self.assertEqual(stat, status_code['OK'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(int(self.max_results), len(ret['entry']))

    # 针对 max_results 的获取音乐评论异常测试函数
    def test_get_reviews_exception_max_results_v1(self):
        invalid_max_results = 'BadMaxResults'  # bad max results
        stat, ret = self.client_v1.music.reviews(self.music_id, self.start_index,\
            invalid_max_results, self.orderby_score)
        ret = json.loads(ret)
        self.assertEqual(stat, status_code['OK'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(10, len(ret['entry']))

        invalid_max_results = '51'  # too big max results > 50
        stat, ret = self.client_v1.music.reviews(self.music_id, self.start_index,\
            invalid_max_results, self.orderby_score)
        ret = json.loads(ret)
        self.assertEqual(stat, status_code['OK'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(50, len(ret['entry']))

        invalid_max_results = '-1'  # too small max results
        stat, ret = self.client_v1.music.reviews(self.music_id, self.start_index,\
            invalid_max_results, self.orderby_score)
        ret = json.loads(ret)
        self.assertEqual(stat, status_code['OK'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(0, len(ret['entry']))        

    # 针对 orderby 的获取音乐评论异常测试函数
    def test_get_reviews_exception_orderby_v1(self):
        invalid_orderby = 'BadOrderBy'  # bad orderby method
        stat, ret = self.client_v1.music.reviews(self.music_id, self.start_index,\
            self.max_results, invalid_orderby)
        ret = json.loads(ret)
        self.assertEqual(stat, status_code['OK'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(int(self.max_results), len(ret['entry']))         
    
    # 针对 music_id 的发布音乐评论异常测试函数
    def test_new_review_exception_music_id_v2(self):
        invalid_music_id = '1000000000000' # wrong music id
        stat, ret = self.client_v2.music.review.new(invalid_music_id,\
         self.title, self.content)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertEqual('music_not_found', ret['msg'])
        self.assertEqual(7000, ret['code'])        
        
        invalid_music_id = 'abcdefg' # bad music id
        stat, ret = self.client_v2.music.review.new(invalid_music_id, \
            self.title, self.content)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertEqual('music_not_found', ret['msg'])
        self.assertEqual(7000, ret['code'])        

        invalid_music_id = '' # empty music id
        stat, ret = self.client_v2.music.review.new(invalid_music_id, self.title, \
            self.content)        
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        # check str and code
        self.assertEqual('missing_args', ret['msg'])
        self.assertEqual(1002, ret['code'])
        
    # 针对 title 的发布音乐评论异常测试函数
    def test_new_review_exception_title_v2(self): 
        invalid_title = self.title*200 # too long title
        #pdb.set_trace()
        stat, ret = self.client_v2.music.review.new(self.music_id, \
            invalid_title, self.content)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['CREATED'])
        self.assertTrue(invalid_title.startswith(ret['title']))
        review_id = ret['id']
        ret = self.client_v2.music.review.delete(review_id)
        self.assertEqual('OK', ret)

        invalid_title = "" # empty title
        stat, ret = self.client_v2.music.review.new(self.music_id, invalid_title, \
            self.content)
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('missing_args', ret['msg'])
        self.assertEqual(1002, ret['code'])        

    # 针对 content 的发布音乐评论异常测试函数
    def test_new_review_exception_content_v2(self):
        invalid_content = "TooShort" # too short content
        stat, ret = self.client_v2.music.review.new(self.music_id, \
            self.title, invalid_content)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertEqual('review_content_short(should more than 150)', \
            ret['msg'])
        self.assertEqual(7004, ret['code'])            

        invalid_content = "" # empty title
        stat, ret = self.client_v2.music.review.new(self.music_id, self.title, \
            invalid_content)
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('missing_args', ret['msg'])
        self.assertEqual(1002, ret['code'])

    # 针对 rating 的发布音乐评论异常测试函数
    def test_new_review_exception_rating_v2(self):
        invalid_rating = "BadRating" # bad rating
        stat, ret = self.client_v2.music.review.new(self.music_id, self.title, \
        self.content, invalid_rating)  # attention!!!! no rating error answer
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['CREATED'])
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)
        review_id = ret['id']
        stat, ret = self.client_v2.music.review.delete(review_id)

        invalid_rating = "-1" # too small rating
        stat, ret = self.client_v2.music.review.new(self.music_id, self.title, \
        self.content, invalid_rating)  # attention!!!! no rating error answer
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['CREATED'])
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)
        review_id = ret['id']
        stat, ret = self.client_v2.music.review.delete(review_id)
        
        invalid_rating = "6" # too big rating
        stat, ret = self.client_v2.music.review.new(self.music_id, self.title, \
        self.content, invalid_rating)  # attention!!!! no rating error answer
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['CREATED'])
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)
        review_id = ret['id']
        stat, ret = self.client_v2.music.review.delete(review_id)

    # 针对 review_id 的更新音乐评论异常测试函数
    def test_update_review_exception_review_id_v2(self):  
        invalid_review_id = 'BadReviewId' # bad review id
        content = self.content * 2
        stat, ret = self.client_v2.music.review.update(invalid_review_id,\
         self.title, content)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertEqual('invalid_request_uri', ret['msg'])
        self.assertEqual(107, ret['code'])

        invalid_review_id = '1000000000' # wrong review id
        content = self.content * 2
        stat, ret = self.client_v2.music.review.update(invalid_review_id, \
            self.title, content)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertEqual('review_not_found', ret['msg'])
        self.assertEqual(7006, ret['code'])

        invalid_review_id = "" # empty review id
        content = self.content * 2
        stat, ret = self.client_v2.music.review.update(invalid_review_id, \
            self.title, content)
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('invalid_request_uri', ret['msg'])
        self.assertEqual(107, ret['code'])
    
    # 针对 title 的更新音乐评论异常测试函数
    def test_update_review_exception_title_v2(self):
        stat, ret = self.client_v2.music.review.new(self.music_id, self.title,\
         self.content)
        review_id = ret['id']
        # update
        invalid_title = self.title*200 # too long title
        stat, ret = self.client_v2.music.review.update(review_id, invalid_title,\
         self.content)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['ACCEPTED'])
        self.assertTrue(invalid_title.startswith(ret['title']))
        invalid_title = "" # empty title
        stat, ret = self.client_v2.music.review.update(review_id, invalid_title, \
            self.content)
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('missing_args', ret['msg'])
        self.assertEqual(1002, ret['code'])
        stat, ret = self.client_v2.music.review.delete(review_id)
        
    # 针对 content 的更新音乐评论异常测试函数
    def test_update_review_exception_content_v2(self):
        stat, ret = self.client_v2.music.review.new(self.music_id, self.title,\
         self.content)
        review_id = ret['id']
        # update
        invalid_content = "TooShort" # too short content
        stat, ret = self.client_v2.music.review.update(review_id, self.title,\
         invalid_content)
        try:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(stat, status_code['ACCEPTED'])
            self.assertTrue(ret.has_key('msg') and (ret['msg']==\
                'review_content_short(should more than 150)'))
        finally:
            stat, ret = self.client_v2.music.review.delete(review_id)
    
    # 针对 rating 的更新音乐评论异常测试函数
    def test_update_review_exception_rating_v2(self): 
        stat, ret = self.client_v2.music.review.new(self.music_id, \
            self.title, self.content)
        review_id = ret['id']

        invalid_rating = "BadRating" # bad rating
        stat, ret = self.client_v2.music.review.update(review_id, \
            self.title, self.content, invalid_rating) 
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['ACCEPTED'])
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)

        invalid_rating = "-1" # too small rating
        stat, ret = self.client_v2.music.review.update(review_id, \
        self.title, self.content, invalid_rating) 
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['ACCEPTED'])
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)
        
        invalid_rating = "6" # too big rating
        stat, ret = self.client_v2.music.review.update(review_id, \
        self.title, self.content, invalid_rating) 
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['ACCEPTED'])
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)

        # delete
        review_id = ret['id']
        ret = self.client_v2.music.review.delete(review_id)
    
    # 针对 review_id 的删除音乐评论异常测试函数
    def test_delete_review_exception_review_id_v2(self):
        invalid_review_id = "BadReviewId" # bad review id
        stat, ret = self.client_v2.music.review.delete(invalid_review_id)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertEqual('invalid_request_uri', ret['msg'])
        self.assertEqual(107, ret['code'])

        invalid_review_id = '1000000000' # wrong review id
        stat, ret = self.client_v2.music.review.delete(invalid_review_id)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(stat, status_code['NOT_FOUND'])
        self.assertEqual('review_not_found', ret['msg'])
        self.assertEqual(7006, ret['code'])

        invalid_review_id = '' # empty review id
        stat, ret = self.client_v2.music.review.delete(invalid_review_id)
        self.assertEqual(stat, status_code['BAD_REQUEST'])
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual('invalid_request_uri', ret['msg'])
        self.assertEqual(107, ret['code'])
    
if __name__ == '__main__':
    main(testRunner=test_runner())