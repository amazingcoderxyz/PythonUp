#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by charles on 2019-08-28
# Function: 

import logging
from log_config import log_config
log_config.init_log_config()
logger = logging.getLogger()
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("selenium").setLevel(logging.ERROR)
logging.getLogger("requests").setLevel(logging.ERROR)
logging.getLogger("selenium").setLevel(logging.ERROR)
logging.getLogger("lxml").setLevel(logging.ERROR)
logging.getLogger("beautifulsoup4").setLevel(logging.ERROR)

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.96 Safari/537.36",
    "accept-language": "zh-CN,zh;q=0.9",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "referer": "https://www.zhipin.com/job_detail/?query=c&city=101010100&industry=&position="

}

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "H911PVTH8L6OL79D"
proxyPass = "D5DF0D375323D611"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

ip = "61.178.149.237"
port = 59042
proxyMeta = "https://{ip}:{port}".format(ip=ip, port=port)
proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}


def str2cookies(str_cookies):
    cookies = {}
    list_item = str_cookies.strip().split(";")
    for coo in list_item:
        item = coo.split("=")
        cookies[item[0].strip()] = item[1].strip()

    return cookies
