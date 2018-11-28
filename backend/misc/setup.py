import sys
sys.path.insert(0, '.')

import binascii
import os
from typing import Optional


main_path = os.path.abspath(os.path.join(__file__, '../..'))
private_path = os.path.join(main_path, 'private.py')


def is_already_setup() -> Optional[bool]:
    if os.path.exists(private_path):
        return True


def setup_config():
    print('Setting up private config...')
    frontend_salt = '%r' % binascii.hexlify(os.urandom(32))

    extra = """
##########################################
# 可选 - 邮件发送配置，默认关闭注册邮件
##########################################

EMAIL_ENABLE = False
EMAIL_ACTIVATION_ENABLE = False
EMAIL_SENDER = 'Icarus 社区程序'
EMAIL_HOST = 'smtp.xxx.com'
EMAIL_PORT = 465
EMAIL_USE_TLS = True
EMAIL_USERNAME = 'user'
EMAIL_PASSWORD = 'pasword'

##########################################
# 可选配置 - 开启搜索功能（需要Elasticsearch）
##########################################

SEARCH_ENABLE = False
ES_INDEX_NAME = 'icarus-index'
ES_HOSTS = [{
    "host": "localhost",
    "port": 9200
}]

##########################################
# 可选 - 文件上传（七牛配置）
##########################################

UPLOAD_ENABLE = False
UPLOAD_STATIC_HOST = ''
UPLOAD_BACKEND = 'qiniu'
UPLOAD_QINIU_ACCESS_KEY = 'PLACE_HOLDER'
UPLOAD_QINIU_SECRET_KEY = 'PLACE_HOLDER'
UPLOAD_QINIU_BUCKET = 'PLACE_HOLDER'
UPLOAD_QINIU_SAVEKEY = '$(etag)'
UPLOAD_QINIU_DEADLINE_OFFSET = 3600  # 上传key有效时间 10分钟
UPLOAD_QINIU_MIME_LIMIT = 'image/*'  # 默认只允许上传图片
UPLOAD_QINIU_CALLBACK_URL = 'PLACE_HOLDER'  # 开启时必填，七牛上传回调地址
UPLOAD_FILE_SIZE_MIN = 100  # 文件必须大于100字节
UPLOAD_FILE_SIZE_MAX = 3 * 1024 * 1024  # 文件必须小于3MB

UPLOAD_QINIU_IMAGE_TOPIC_STYLE = ''  # 文章页面图片所用的七牛图片样式

"""

    f = open(private_path, 'w', encoding='utf-8')
    f.write('\n'.join([
        "import logging",
        "",
        "# 站点名称",
        "SITE_NAME = 'Icarus'",
        "# 站点地址，末尾不要带 /",
        "SITE_URL = 'http://localhost:8080'",
        "# 管理员联系邮箱，用于用户回报站点错误",
        "SITE_CONTACT_EMAIL = 'manage@mail.com'",
        "",
        "HOST = '127.0.0.1'",
        "PORT = 9999",
        "DEBUG_LEVEL = logging.DEBUG",
        "CORS_OPTIONS = CORSOptions('*', allow_credentials=True, expose_headers='*', allow_headers='*')",
        "",
        "# PostgreSQL 数据库地址",
        "DATABASE_URI = 'postgresql://icarus:IcaruStest123@localhost/icarus'",
        "",
        "# REDIS 数据库地址",
        "REDIS_HOST = 'localhost'",
        "REDIS_PORT = 6379",
        "",
        "# 前端密码盐，已经自动生成为随机值",
        f"USER_SECURE_AUTH_FRONTEND_SALT = {frontend_salt}",
        "",
        extra
    ]))
    print('%s generated.' % private_path)
    print('Please edit private.py before run main.py next time.')
    print('Exited.')
    quit()


if not is_already_setup():
    setup_config()
