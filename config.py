import logging
import redis

class Config(object):
    """工程配置信息"""
    DEBUG = True
    # define the database
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/news'
    SQLALCHEMY_TRACK_MODIFICAIONS = False

    # define the redise
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # define the session
    SECRET_KEY = 'n2XRiaaDqZUuNMExwlXijpgADx7j7epGVBBwmIaAsfRMpXLjmLr4cA=='
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True  # let the session_id protect b the secret
    SESSION_REDIS = redis.StrictRedis(host = REDIS_HOST, port = REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400  # s thats mean one day

    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    LOG_LEVEL = logging.ERROR


# factory
config = {
    "development":  DevelopmentConfig,
    "production": ProductionConfig
}