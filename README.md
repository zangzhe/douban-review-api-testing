### douban-review-api-testing
```
douban-review-api-testing 是针对 douban 评论 API 的测试程序。测试框架基于
douban-client-0.0.6，权限认证基于 OAuth 2.0。
```


### 使用说明
```
## 安装
$ cd douban-review-api-testing/
$ python setup.py install

## 运行
$ cd douban-review-api-testing/tests/
$ vim test_config.py  # 配置 test_config.py 中参数 
$ python run.py  # 批量运行所有 case
$ python test_api_user_review.py # 运行指定 case
$ python test_api_user_reveiw.py TestApiUserReview.test_get_reviews_function_v1 # 运行指定测试方法

## 结果
标准输出打印当前测试进度，例如：
[Running] __main__.TestApiBookReview.test_delete_review_exception_review_id_v2
[Running] __main__.TestApiBookReview.test_get_reviews_exception_book_id_v1
[Running] __main__.TestApiBookReview.test_get_reviews_exception_isbn_id_v1

日志文件中以 python unittest 输出格式记录结果细节，例如：
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
问：case 代码中函数的 v1，v2 后缀是什么意思？
答：v1 代表该测试针对 v1 版本接口，v2 代表该测试针对 v2 版本接口。

5.
问：使用自己豆瓣账号申请的 api key，在引导用户授权后，为何依然无法获取有效
access_token？
答：请确保在您的豆瓣上添加了该测试用户，详情见 douban api v2 相关文档。

6.
问：为何会有一些测试 FAIL 掉的情况？
答：正常情况下，应该有11个 FAIL 测试，问题涉及 status code、error_code、
json数据内容，个人认为均为 bug：
FAIL: test_update_review_exception_content_v2 (tests.test_api_book_review.TestApiBookReview)
FAIL: test_new_review_exception_title_v2 (tests.test_api_movie_review.TestApiMovieReview)
FAIL: test_update_review_exception_content_v2 (tests.test_api_movie_review.TestApiMovieReview)
FAIL: test_update_review_exception_title_v2 (tests.test_api_movie_review.TestApiMovieReview)
FAIL: test_get_reviews_exception_max_results_v1 (tests.test_api_music_review.TestApiMusicReview)
FAIL: test_new_review_exception_content_v2 (tests.test_api_music_review.TestApiMusicReview)
FAIL: test_new_review_exception_music_id_v2 (tests.test_api_music_review.TestApiMusicReview)
FAIL: test_new_review_exception_title_v2 (tests.test_api_music_review.TestApiMusicReview)
FAIL: test_update_review_exception_content_v2 (tests.test_api_music_review.TestApiMusicReview)
FAIL: test_update_review_exception_review_id_v2 (tests.test_api_music_review.TestApiMusicReview)
FAIL: test_update_review_exception_title_v2 (tests.test_api_music_review.TestApiMusicReview)

7.
问：测试中 case 报 ERROR 或大量 FAIL。
答：原因可能涉及网络环境、douban 封禁、账号 token 过期等，将我遇到过的问题罗列如下，
可以在日志文件中搜索这些关键词以帮助定位问题：
access_token_has_expired  # token 过期(有效期一周)，需要重新申请
rate_limit_exceeded1  # 请求频率过高，douban 限制访问频率为 40 qps。
rate_limit_exceeded2  # IP访问速度限制
user_has_blocked  # 用户已被 douban 封禁
socket.error  # 通信错误，与当前网络环境相关
Errno 10060   # 通信错误，与当前网络环境相关
Errno 10054   # 通信错误，与当前网络环境相关
CannotSendRequest()  # 通信错误，与当前网络环境相关
```


### Changelog
```
__v0.0.5 [2014-03-27]__
* 增加配置功能，并添加若干 douban 测试账户
* 增加日志记录测试结果
* 完善 README
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
