# -*- coding: utf-8 -*-

import os
import sys

from six import print_
from six.moves import input, reduce


TEST_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)
sys.path.insert(0, ROOT_DIR)

from unittest import main, TestCase
from douban_client import DoubanClient
from douban_client.api.error import DoubanAPIError
import httplib, json

class DoubanClient_v1():
    api_server = "api.douban.com"
    def __init__(self):
        self.conn = httplib.HTTPConnection(DoubanClient_v1.api_server)

    def get(self, url):
        try:
            self.conn.request("GET", url)
            r = self.conn.getresponse()
        except httplib.BadStatusLine, httplib.CannotSendRequest:
            self.conn.close()
            self.conn = httplib.HTTPConnection(DoubanClient_v1.api_server)
            self.conn.request("GET", url)
            r = self.conn.getresponse()            
        #print r1.status, r1.reason

        data = r.read()
        return data

try:
    from local_config import KEY, SECRET, CALLBACK, SCOPE, TOKEN
except ImportError:
    KEY = '008c9529361828e901a5bf7ba2487abb'
    SECRET = 'b13c7ae9e656b793'
    CALLBACK = ''

    SCOPE_MAP = { 'basic': ['douban_basic_common', 'community_basic_user'], }
    SCOPE = ','.join(reduce(lambda x, y: x + y, SCOPE_MAP.values()))
    TOKEN = '0b8d6971ffb8f53722a83c55ff2adfa5'

def get_client_v2():
    client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)

    token = TOKEN

    if token:
        client.auth_with_token(token)
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
    def client_v2(self):
        return client_v2
    @property
    def client_v1(self):
        return client_v1