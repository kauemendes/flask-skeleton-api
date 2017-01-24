#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    config
    ~~~~~~
    Application-wide configurations.
    You can put whatever you want here. The convention is to write configuration
    variables in upper-case.

    :see http://flask.pocoo.org/docs/config/
    :author: Jeff Kereakoglow
    :date: 2014-11-14
    :copyright: (c) 2014 by Alexis Digital
    :license: MIT, see LICENSE for more details
"""
import os

_basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    """Base configuration."""
    SECRET_KEY = 'my_precious'
    APP_NAME = "Flask Skeleton"
    DEBUG = True
    CACHE_TIMEOUT = 60 * 60 * 15
    BCRYPT_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    BLUEMIX_STS_USERNAME = '55b6c577-1bd0-4072-a2b3-9770c2c9947f'
    BLUEMIX_STS_PASSWORD = 'ZlsEd3fbWQlj'
    BLUEMIX_TSS_USERNAME = '5641e753-cabe-4893-a93a-2a802e9a8cc6'
    BLUEMIX_TSS_PASSWORD = 'QpEM5uoBapc3'
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@127.0.0.1/x"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG_TB_ENABLED = True


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@127.0.0.1/x"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG_TB_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@127.0.0.1/x"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    DEBUG_TB_ENABLED = False