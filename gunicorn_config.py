# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 10:25
# @Author  : OKC

# 日志配置
loglevel = "debug"
accesslog = 'log/access.log'
errorlog = 'log/error.log'

workers = 4
# 设置工作模式为协程
worker_class = "gevent"
bind = "0.0.0.0:7456"