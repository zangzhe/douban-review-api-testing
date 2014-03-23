### douban-review-api-testing
```
douban-review-api-testing 是针对 douban 评论 API 的测试程序。测试框架基于
douban-client-0.0.6，权限认证基于 OAuth 2.0。
```


### douban 评论接口列表及测试覆盖情况：
```
  API描述                      测试覆盖情况 
* 获取指定评论ID的评论         覆盖 api v1 版本
* 获取指定用户的所有评论       覆盖 api v1 版本
* 获取指定书籍的所有评论       覆盖 api v1 版本     
* 发布指定书籍的评论           覆盖 api v2 版本
* 更新指定书籍的评论           覆盖 api v2 版本
* 删除指定书籍的评论           覆盖 api v2 版本
* 获取指定电影的所有评论       未覆盖
* 发布指定电影的评论           覆盖 api v2 版本
* 更新指定电影的评论           覆盖 api v2 版本
* 删除指定电影的评论           覆盖 api v2 版本
* 获取指定音乐的所有评论       覆盖 api v1 版本
* 发布指定音乐的评论           覆盖 api v2 版本
* 更新指定音乐的评论           覆盖 api v2 版本
* 删除指定音乐的评论           覆盖 api v2 版本
```


### 安装
```
确保已正确安装python2.7.x和setuptools，并接入互联网。
进入安装程序根目录，运行如下命令进行安装：
python setup.py install
```


### 使用说明
```
## OAuth 2.0 认证
在 module根目录/tests/framewrk.py 中设定有效的 KEY, SECRET, CALLBACK, 
SCOPE_MAP, SCOPE，TOKEN等参数。

## 运行
进入 module根目录/tests/，运行如下命令：
python run.py
若要运行单独case，可运行如下类似命令：
python test_api_xxx_review.py

## 测试结果
使用python unitest的输出格式：
.   测试PASS
F   测试FAIL
E   测试ERROR
针对测试中的 FAIL 和 ERROR，会打印出详细的细节，某次执行的结果举例：
C:\Python27\douban\douban-client-0.0.6(v2)\douban-client-0.0.6\tests>python run.
py
............F.........................
======================================================================
FAIL: test_update_review_exception_content_v2 (tests.test_api_book_review.TestAp
iBookReview)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Python27\douban\douban-client-0.0.6(v2)\douban-client-0.0.6\tests\tes
t_api_book_review.py", line 310, in test_update_review_exception_content_v2
    'review_content_short(should more than 150)'))
AssertionError: False is not true

======================================================================
Ran 41 tests in 36.549s

FAILED (failures=1)
```


### 用例说明
```
## TestApiIdReview 特定ID评论接口测试类 (2 tests)
test_get_reviews_function_v1  获取特定ID评论功能测试函数
test_get_reviews_exception_user_id_v1  针对 review_id 的获取评论异常测试函数

## TestApiUserReview 用户评论接口测试类 (5 tests)
test_get_reviews_function_v1  获取特定用户评论功能测试函数
test_get_reviews_exception_user_id_v1  针对 user_id 的获取用户评论异常测试函数
test_get_reviews_exception_start_index_v1  针对 start_index 的获取用户评论异常测试函数
test_get_reviews_exception_max_results_v1  针对 max_results 的获取用户评论异常测试函数
test_get_reviews_exception_orderby_v1  针对 orderby 的获取用户评论异常测试函数

## TestApiBookReview 图书评论接口测试类 (16 tests)
test_get_reviews_function_v1  获取图书评论功能测试函数
test_new_update_delete_review_function_v2  增删改图书评论功能测试函数
test_get_reviews_exception_book_id_v1  针对 book_id 的获取图书评论异常测试函数
test_get_reviews_exception_isbn_id_v1  针对 isbn_id 的获取图书评论异常测试函数
test_get_reviews_exception_start_index_v1  针对 start_index 的获取图书评论异常测试函数
test_get_reviews_exception_max_results_v1  针对 max_results 的获取图书评论异常测试函数
test_get_reviews_exception_orderby_v1  针对 orderby 的获取图书评论异常测试函数
test_new_review_exception_book_id_v2  针对 book_id 的发布图书评论异常测试函数
test_new_review_exception_title_v2  针对 title 的发布图书评论异常测试函数
test_new_review_exception_content_v2  针对 content 的发布图书评论异常测试函数
test_new_review_exception_rating_v2  针对 rating 的发布图书评论异常测试函数
test_update_review_exception_review_id_v2  针对 review_id 的更新图书评论异常测试函数
test_update_review_exception_title_v2  针对 title 的更新图书评论异常测试函数
test_update_review_exception_content_v2  针对 content 的更新图书评论异常测试函数
test_update_review_exception_rating_v2  针对 rating 的更新图书评论异常测试函数
test_delete_review_exception_review_id_v2  针对 review_id 的删除图书评论异常测试函数

## TestApiMovieReview 电影评论接口测试类 (10 tests)
test_new_update_delete_review_function_v2  增删改电影评论功能测试函数
test_new_review_exception_movie_id_v2  针对 movie_id 的发布电影评论异常测试函数
test_new_review_exception_title_v2  针对 title 的发布电影评论异常测试函数
test_new_review_exception_content_v2  针对 content 的发布电影评论异常测试函数
test_new_review_exception_rating_v2  针对 rating 的发布电影评论异常测试函数
test_update_review_exception_review_id_v2  针对 review_id 的更新电影评论异常测试函数
test_update_review_exception_title_v2  针对 title 的更新电影评论异常测试函数
test_update_review_exception_content_v2  针对 content 的更新电影评论异常测试函数
test_update_review_exception_rating_v2  针对 rating 的更新电影评论异常测试函数
test_delete_review_exception_review_id_v2  针对 review_id 的删除电影评论异常测试函数

## TestApiMusicReview 音乐评论接口测试类 (15 tests)
test_get_reviews_function_v1  获取音乐评论功能测试函数
test_new_update_delete_review_function_v2  增删改音乐评论功能测试函数
test_get_reviews_exception_music_id_v1  针对 music_id 的获取音乐评论异常测试函数
test_get_reviews_exception_start_index_v1  针对 start_index 的获取音乐评论异常测试函数
test_get_reviews_exception_max_results_v1  针对 max_results 的获取音乐评论异常测试函数
test_get_reviews_exception_orderby_v1  针对 orderby 的获取音乐评论异常测试函数
test_new_review_exception_music_id_v2  针对 music_id 的发布音乐评论异常测试函数
test_new_review_exception_title_v2  针对 title 的发布音乐评论异常测试函数
test_new_review_exception_content_v2  针对 content 的发布音乐评论异常测试函数
test_new_review_exception_rating_v2  针对 rating 的发布音乐评论异常测试函数
test_update_review_exception_review_id_v2  针对 review_id 的更新音乐评论异常测试函数
test_update_review_exception_title_v2  针对 title 的更新音乐评论异常测试函数
test_update_review_exception_content_v2  针对 content 的更新音乐评论异常测试函数
test_update_review_exception_rating_v2  针对 rating 的更新音乐评论异常测试函数
test_delete_review_exception_review_id_v2  针对 review_id 的删除音乐评论异常测试函数
```


### FAQ
```
1. 
问：为什么有的测试针对 api v1，有的针对 api v2 版本呢？
答：依照题目要求，最初是需要测试　v1 版本的，但我用自己的豆瓣账户申请
api key 并尝试 OAuth 1.0 下授权连接 v1 api 失败，总返回 invalid consumer
错误，请教豆瓣上相关话题后，发现貌似现在新申请的 api key 已经只能适用于
OAuth 2.0，考虑到版本问题应该不是本次测试的主要问题点，并且 api v2 中已经
关闭或者限制了针对特定 subject 获取所有评论的接口，所以我对无需授权接口
（查询接口）在 api v1 版本上测试，对需要授权接口（增删改接口）在 api v2 版
本上测试。

2.
问：测试用例为什么不能覆盖获取指定电影的所有评论这个接口？   
答：使用 api v1 接口测试，会提示接口已经停用，而 api v2 针对普通用户目前
还没有开放电影、图书、音乐的查询接口。

3.
问：在获取指定图书、电影、音乐的评论测试中，为什么只能获取内容摘要？
答：因为是在 api v1 版本的未授权模式下进行测试的，只能获取 summary。

4.
问：程序安装到哪里了？
答：我在 windows 环境下python安装在 c 盘根目录，安装后模块的路径为
C:\Python27\Lib\site-packages\douban_review_api_testing-0.0.1-py2.7.egg。

5.
问：case 代码中函数的 v1，v2 后缀是什么意思？
答：v1 代表该测试针对 v1 版本接口，v2 代表该测试针对 v2 版本接口。


6.
问：使用自己豆瓣账号申请的 api key，在引导用户授权后，为何依然无法获取有效
access_token？
答：请确保在您的豆瓣上添加了该测试用户，详情见 douban api v2 相关文档。

7.
问：为何会有一些测试 FAIL 掉的情况？
答：在我的反复测试中，目前存在四个测试 FAIL 的情况：前三个是更新图书、电影、
音乐的评论内容长度没有校验，导致可以发很短的评论，个人认为这是个 bug；最后
一个是获取音乐所有评论时候，默认条目应该是50，但实际却为36，个人认为可能是
老接口停用，受到限制或者不再维护。
FAIL case 的详情：
======================================================================
FAIL: test_update_review_exception_content_v2 (tests.test_api_book_review.TestAp
iBookReview)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Python27\douban\douban-client-0.0.6(v2)\douban-client-0.0.6\tests\tes
t_api_book_review.py", line 310, in test_update_review_exception_content_v2
    'review_content_short(should more than 150)'))
AssertionError: False is not true

======================================================================
FAIL: test_update_review_exception_content_v2 (tests.test_api_movie_review.TestA
piMovieReview)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Python27\douban\douban-client-0.0.6(v2)\douban-client-0.0.6\tests\tes
t_api_movie_review.py", line 162, in test_update_review_exception_content_v2
    'review_content_short(should more than 150)'))
AssertionError: False is not true

======================================================================
FAIL: test_get_reviews_exception_max_results_v1 (tests.test_api_music_review.Tes
tApiMusicReview)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Python27\douban\douban-client-0.0.6(v2)\douban-client-0.0.6\tests\tes
t_api_music_review.py", line 142, in test_get_reviews_exception_max_results_v1
    self.assertEqual(50, len(ret['entry']))
AssertionError: 50 != 36

======================================================================
FAIL: test_update_review_exception_content_v2 (tests.test_api_music_review.TestA
piMusicReview)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Python27\douban\douban-client-0.0.6(v2)\douban-client-0.0.6\tests\tes
t_api_music_review.py", line 289, in test_update_review_exception_content_v2
    'review_content_short(should more than 150)'))
AssertionError: False is not true

----------------------------------------------------------------------

8.
问：测试中大量 case 报 ERROR 和 FAIL，返回报中有 rate_limit_exceeded1 以及
大量的内容无法获取错误。
答： 豆瓣官方对普通用户的访问次数设限，通常为 40 次每分钟，频繁执行测试，很可能
导致临时性被禁用。可以重启计算机或者等待几个小时，就会解禁。

9.
问：测试总大量 case 报 ERROR，返回报错 access_token_has_expired。
答：access_token 过期，需要重新手动获取（我尝试使用 refresh access code 的接口，但每次都失败）。

```


### TODO
```
1. 测试用例补充。
2. refresh_access_code 接口生效
```


### Changelog
```
__v0.0.4 [2014-03-23]__
* 针对 api v1 接口进行封装，降低代码耦合性
* 增加对获取特定id评论接口的测试用例
__v0.0.3 [2014-03-14]__
* 针对 api 返回值，增加对 status code, error code 的测试
* 增加对空参数的异常测试
* 删除了我自己的 api key 等用户认证
__v0.0.2 [2014-03-04]__ 
* 增加对 api v1 用户评论接口的测试
* 调整代码结构
* 跟新了 access_token
__v0.0.1 [2014-02-26]__
* 根据豆瓣 API v2 文档，发布第一个版本
```


### 联系
* 使用 douban-review-api-testing 过程中遇到 bug, 可以反馈邮箱地址
zang_zhe@163.com
