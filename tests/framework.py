# -*- coding: utf-8 -*-

import os
import sys

from six import print_
from six.moves import input, reduce

status_code = {'OK':200, 'CREATED':201, 'ACCEPTED':202, 'BAD_REQUEST':400,\
'UNAUTHORIZED':401, 'FORBIDDEN':403, 'NOT_FOUND':404, 'INTERNAL_SERVER_ERROR':500}

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)
sys.path.insert(0, ROOT_DIR)

from unittest import main, TestCase
from douban_client import DoubanClient, DoubanClient_v1
from douban_client.api.error import DoubanAPIError


SCOPE_MAP = { 'basic': ['douban_basic_common', 'community_basic_user'], }
SCOPE = ','.join(reduce(lambda x, y: x + y, SCOPE_MAP.values()))


try:
    from test_config import KEY, SECRET, CALLBACK, TOKEN
except ImportError:
    KEY = ''
    SECRET = ''
    CALLBACK = ''
    TOKEN = ''

def get_client_v2():
    client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)

    token = TOKEN

    if token:
        client.auth_with_token(token)
        #refresh_token_code = REFRESH_TOKEN
        #client.refresh_token(refresh_token_code)
    else:
        print_('Go to the following link in your browser:')
        print_(client.authorize_url)

        code = input('Enter the verification code and hit ENTER when you\'re done:')
        client.auth_with_code(code)
        print_('token code:', client.token_code)
        print_('refresh token code:', client.refresh_token_code)
    return client

client_v1 = DoubanClient_v1()
client_v2 = get_client_v2()

class DoubanClientTestBase(TestCase):
    def setUp(self):
        pass

    @property
    def client_v1(self):
        return client_v1
        
    @property
    def client_v2(self):
        return client_v2
