# -*- coding: utf-8 -*-

import os
import sys

from six import print_
from six.moves import input, reduce
import ConfigParser, pdb, time

status_code = {'OK':200, 'CREATED':201, 'ACCEPTED':202, 'BAD_REQUEST':400,\
'UNAUTHORIZED':401, 'FORBIDDEN':403, 'NOT_FOUND':404, 'INTERNAL_SERVER_ERROR':500}

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)
sys.path.insert(0, ROOT_DIR)

from unittest import main, TestCase, TextTestRunner
from douban_client import DoubanClient, DoubanClient_v1
from douban_client.api.error import DoubanAPIError


SCOPE_MAP = { 'basic': ['douban_basic_common', 'community_basic_user'], }
SCOPE = ','.join(reduce(lambda x, y: x + y, SCOPE_MAP.values()))

config=ConfigParser.ConfigParser()  
with open('test_config.cfg', 'r+') as cfgfile:  
    config.readfp(cfgfile)  
    
    log_name = config.get('INFO', 'log_name')
    key = config.get('INFO', 'key')
    secret = config.get('INFO', 'secret')
    callback = config.get('INFO', 'callback')
    token = config.get('INFO', 'token')
    refresh_token = config.get('INFO', 'refresh_token')
    expires_at = config.get('INFO', 'expires_at')

def get_client_v2():
    client = DoubanClient(key, secret, callback, SCOPE)
    if expires_at:
        expires_time = int(expires_at)

    if token:
        now_time = int(time.time())
        remaining_seconds = expires_time - now_time
        print 'sss: ' + str(remaining_seconds)
        if remaining_seconds > 3600:
            client.auth_with_token(token)
        else:
            client.refresh_token(refresh_token)   
            config.set('INFO', 'token', client.token_code)
            config.set('INFO', 'refresh_token', client.refresh_token_code)
            config.set('INFO', 'expires_at', client.expires_at)
            with open('test_config.cfg', 'wb') as configfile:
                config.write(configfile)
    else:
        print_('Go to the following link in your browser:')
        print_(client.authorize_url)

        code = input('Enter the verification code and hit ENTER when you\'re done:')
        client.auth_with_code(code)
        print_('token code:', client.token_code)
        print_('refresh token code:', client.refresh_token_code)
        print_('expires at:', client.expires_at)
        print type(client.expires_at)
        config.set('INFO', 'token', client.token_code)
        config.set('INFO', 'refresh_token', client.refresh_token_code)
        config.set('INFO', 'expires_at', client.expires_at)
        with open('test_config.cfg', 'wb') as configfile:
            config.write(configfile)
        #pdb.set_trace()

    return client

def test_runner():
    log_fd = open(log_name, 'w')
    runner = TextTestRunner(stream=log_fd)
    return runner

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
