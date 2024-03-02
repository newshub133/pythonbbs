class BaseConfig:
    SECRET_KEY = "you secret key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@127.0.0.1:3306/pythonbbs?charset=utf8mb4"


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = ""


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = ""

