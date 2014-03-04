# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, main                            
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
        self.check = True

    # 获取音乐评论功能测试函数
    def test_get_reviews_function_v1(self):
        #print 'test_get_reviews_function_v1'
        url = "/music/subject/"+ self.music_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + self.orderby_score

        ret = self.client_v1.get(url)
        ret = json.loads(ret)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertTrue(self.music_id in ret['link'][0]['@href'])
            self.assertEqual(self.start_index, ret['opensearch:startIndex']['$t'])
            self.assertEqual(self.max_results, ret['opensearch:itemsPerPage']['$t'])

        #jdata = json.loads(ret)
        #jdata_f = json.dumps(jdata, sort_keys=True,indent=2)
        #print jdata_f

    # 增删改音乐评论功能测试函数
    def test_new_update_delete_review_function_v2(self):
        # new
        ret = self.client_v2.music.review.new(self.music_id, self.title, self.content)

        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)

        review_id = ret['id']

        # update
        content = self.content * 2
        ret = self.client_v2.music.review.update(review_id, self.title, content)
        self.assertEqual(content, ret['content'])

        # delete
        ret = self.client_v2.music.review.delete(review_id)
        self.assertEqual('OK', ret)

    # 针对 music_id 的获取音乐评论异常测试函数
    def test_get_reviews_exception_music_id_v1(self):
        #print 'test_get_reviews_exception_music_id_v1'
        invalid_music_id = 'BaiMusicId'   # bad music id
        url = "/music/subject/"+ invalid_music_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        if self.check:
            self.assertTrue(isinstance(ret, str))
            self.assertEqual('bad subject id', ret)

        invalid_music_id = '1000000000'   # wrong music id
        url = "/music/subject/"+ invalid_music_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        if self.check:
            self.assertTrue(isinstance(ret, str))
            self.assertEqual('wrong subject id', ret)

    # 针对 start_index 的获取音乐评论异常测试函数
    def test_get_reviews_exception_start_index_v1(self):
        #print 'test_get_reviews_exception_start_index_v1'
        invalid_start_index = 'BadStartIndex'  # bad start index
        url = "/music/subject/"+ self.music_id + \
        "/reviews?alt=json&start-index="+ invalid_start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)
        if self.check:
            #pdb.set_trace()
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(int(self.max_results), len(ret['entry']))
        
        invalid_start_index = '10000'  # too big index
        url = "/music/subject/"+ self.music_id + \
        "/reviews?alt=json&start-index="+ invalid_start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(0, len(ret['entry']))

        invalid_start_index = '-1'  # too small start index
        url = "/music/subject/"+ self.music_id + \
        "/reviews?alt=json&start-index="+ invalid_start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(int(self.max_results), len(ret['entry']))

    # 针对 max_results 的获取音乐评论异常测试函数
    def test_get_reviews_exception_max_results_v1(self):
        #print 'test_get_reviews_exception_max_results_v1'
        invalid_max_results = 'BadMaxResults'  # bad max results
        url = "/music/subject/"+ self.music_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + invalid_max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(10, len(ret['entry']))

        invalid_max_results = '51'  # too big max results > 50
        url = "/music/subject/"+ self.music_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + invalid_max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(50, len(ret['entry']))

        invalid_max_results = '-1'  # too small max results
        url = "/music/subject/"+ self.music_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + invalid_max_results +\
        "&orderby=" + self.orderby_score
        ret = self.client_v1.get(url)
        ret = json.loads(ret)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(0, len(ret['entry']))        

    # 针对 orderby 的获取音乐评论异常测试函数
    def test_get_reviews_exception_orderby_v1(self):
        #print 'test_get_reviews_exception_orderby_v1'
        invalid_orderby = 'BadOrderBy'  # bad orderby method
        url = "/music/subject/"+ self.music_id + \
        "/reviews?alt=json&start-index="+ self.start_index +\
        "&max-results=" + self.max_results +\
        "&orderby=" + invalid_orderby
        ret = self.client_v1.get(url)
        ret = json.loads(ret)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(int(self.max_results), len(ret['entry']))         

    # 针对 music_id 的发布音乐评论异常测试函数
    def test_new_review_exception_music_id_v2(self):
        #print 'test_new_review_exception_music_id_v2'
        invalid_music_id = '1000000000000' # wrong music id
        #pdb.set_trace()
        ret = self.client_v2.music.review.new(invalid_music_id, self.title, self.content)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual('music_not_found', ret['msg'])
            self.assertEqual(7000, ret['code'])        
        
        invalid_music_id = 'abcdefg' # bad music id
        ret = self.client_v2.music.review.new(invalid_music_id, self.title, self.content)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual('music_not_found', ret['msg']) #????
            self.assertEqual(7000, ret['code'])        

    # 针对 title 的发布音乐评论异常测试函数
    def test_new_review_exception_title_v2(self): 
        #print 'test_new_review_exception_title_v2'
        invalid_title = self.title*200 # too long title
        #pdb.set_trace()
        ret = self.client_v2.music.review.new(self.music_id, invalid_title, self.content)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertTrue(invalid_title.startswith(ret['title']))
        review_id = ret['id']
        ret = self.client_v2.music.review.delete(review_id)
        self.assertEqual('OK', ret)

    # 针对 content 的发布音乐评论异常测试函数
    def test_new_review_exception_content_v2(self):
        #print 'test_new_review_exception_content_v2'
        invalid_content = "TooShort" # too short content
        #pdb.set_trace()
        ret = self.client_v2.music.review.new(self.music_id, self.title, invalid_content)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual('review_content_short(should more than 150)', \
                ret['msg'])
            self.assertEqual(7004, ret['code'])            

    # 针对 rating 的发布音乐评论异常测试函数
    def test_new_review_exception_rating_v2(self):
        #print 'test_new_review_exception_rating_v2'
        invalid_rating = "BadRating" # bad rating
        ret = self.client_v2.music.review.new(self.music_id, self.title, self.content, invalid_rating)
        if self.check:  # attention!!!! no rating error answer
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(self.content, ret['content'])
            self.assertTrue('author' in ret)
        review_id = ret['id']
        ret = self.client_v2.music.review.delete(review_id)
        self.assertEqual('OK', ret)

        invalid_rating = "-1" # too small rating
        ret = self.client_v2.music.review.new(self.music_id, self.title, self.content, invalid_rating)
        if self.check:  # attention!!!! no rating error answer
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(self.content, ret['content'])
            self.assertTrue('author' in ret)
        review_id = ret['id']
        ret = self.client_v2.music.review.delete(review_id)
        self.assertEqual('OK', ret)
        
        invalid_rating = "6" # too big rating
        ret = self.client_v2.music.review.new(self.music_id, self.title, self.content, invalid_rating)
        if self.check:  # attention!!!! no rating error answer
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(self.content, ret['content'])
            self.assertTrue('author' in ret)
        review_id = ret['id']
        ret = self.client_v2.music.review.delete(review_id)
        self.assertEqual('OK', ret)

    # 针对 review_id 的更新音乐评论异常测试函数
    def test_update_review_exception_review_id_v2(self):  
        #print 'test_new_review_exception_review_id_v2'
        invalid_review_id = 'BadReviewId' # bad review id
        content = self.content * 2
        ret = self.client_v2.music.review.update(invalid_review_id, self.title, content)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual('invalid_request_uri', ret['msg'])
            self.assertEqual(107, ret['code'])

        invalid_review_id = '1000000000' # wrong review id
        content = self.content * 2
        ret = self.client_v2.music.review.update(invalid_review_id, self.title, content)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual('review_not_found', ret['msg'])
            self.assertEqual(7006, ret['code'])
    
    # 针对 title 的更新音乐评论异常测试函数
    def test_update_review_exception_title_v2(self):
        #print 'test_update_review_exception_title_v2'
        ret = self.client_v2.music.review.new(self.music_id, self.title, self.content)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)
        review_id = ret['id']
        # update
        invalid_title = self.title*200 # too long title
        ret = self.client_v2.music.review.update(review_id, invalid_title, self.content)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertTrue(invalid_title.startswith(ret['title']))
        review_id = ret['id']
        ret = self.client_v2.music.review.delete(review_id)
        self.assertEqual('OK', ret)
        
    # 针对 content 的更新音乐评论异常测试函数
    def test_update_review_exception_content_v2(self):
        #print 'test_update_review_exception_content_v2'
        ret = self.client_v2.music.review.new(self.music_id, self.title, self.content)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)
        review_id = ret['id']
        # update
        invalid_content = "TooShort" # too short content
        ret = self.client_v2.music.review.update(review_id, self.title, invalid_content)
        if self.check:
            try:
                self.assertTrue(isinstance(ret, dict))
                self.assertTrue(ret.has_key('msg') and (ret['msg']==\
                    'review_content_short(should more than 150)'))
            finally:
                # delete
                ret = self.client_v2.music.review.delete(review_id)
                self.assertEqual('OK', ret)
    
    # 针对 rating 的更新音乐评论异常测试函数
    def test_update_review_exception_rating_v2(self): 
        #print 'test_update_review_exception_rating_v2'
        ret = self.client_v2.music.review.new(self.music_id, self.title, self.content)
        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.content, ret['content'])
        self.assertTrue('author' in ret)
        review_id = ret['id']

        invalid_rating = "BadRating" # bad rating
        ret = self.client_v2.music.review.update(review_id, self.title, self.content, invalid_rating)
        if self.check:  # attention!!!! no rating error answer
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(self.content, ret['content'])
            self.assertTrue('author' in ret)

        invalid_rating = "-1" # too small rating
        ret = self.client_v2.music.review.update(review_id, self.title, self.content, invalid_rating)
        if self.check:  # attention!!!! no rating error answer
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(self.content, ret['content'])
            self.assertTrue('author' in ret)
        
        invalid_rating = "6" # too big rating
        ret = self.client_v2.music.review.update(review_id, self.title, self.content, invalid_rating)
        if self.check:  # attention!!!! no rating error answer
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual(self.content, ret['content'])
            self.assertTrue('author' in ret)

        # delete
        review_id = ret['id']
        ret = self.client_v2.music.review.delete(review_id)
        self.assertEqual('OK', ret)
    
    # 针对 review_id 的删除音乐评论异常测试函数
    def test_delete_review_exception_review_id_v2(self):
        #print 'test_delete_review_exception_review_id_v2'
        invalid_review_id = "BadReviewId" # bad review id
        ret = self.client_v2.music.review.delete(invalid_review_id)
        #print ret
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual('invalid_request_uri', ret['msg'])
            self.assertEqual(107, ret['code'])

        invalid_review_id = '1000000000' # wrong review id
        ret = self.client_v2.music.review.delete(invalid_review_id)
        if self.check:
            self.assertTrue(isinstance(ret, dict))
            self.assertEqual('review_not_found', ret['msg'])
            self.assertEqual(7006, ret['code'])

if __name__ == '__main__':
    main()
