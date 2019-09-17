#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by charles on 2019-08-30
# Function: 

from Crawl.Boss.web_actions import BossActions
import datetime
import urllib.parse
from Crawl.Boss.parse import data2csv
from Crawl.config import logger
import schedule
import time

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.96 Safari/537.36",
    "accept-language": "zh-CN,zh;q=0.9",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "referer": "https://www.zhipin.com/job_detail/?query=c&city=101010100&industry=&position=",
    "device": "Nexus 10"

}

hot_city = [
    {
        "code": 100010000,
        "name": u"全国",
    },
    {
        "code": 101010100,
        "name": u"北京",
    },
    {
        "code": 101020100,
        "name": u"上海",
    },
    {
        "code": 101280100,
        "name": u"广州",
    },
    {
        "code": 101280600,
        "name": u"深圳",
    },
    {
        "code": 101210100,
        "name": u"杭州",
    },
    {
        "code": 101030100,
        "name": "天津",
    },
    {
        "code": 101110100,
        "name": u"西安",
    },
    {
        "code": 101190400,
        "name": u"苏州",
    },
    {
        "code": 101200100,
        "name": u"武汉",
    },
    {
        "code": 101230200,
        "name": u"厦门",
    },
    {
        "code": 101250100,
        "name": u"长沙",
    },
    {
        "code": 101270100,
        "name": "成都",
    },
    {
        "code": 101180100,
        "name": u"郑州",
    },
    {
        "code": 101040100,
        "name": u"重庆",
    }
]


def run_task(query_key, city_num, page, industry='', position='', headless=0):
    query_key_url = urllib.parse.quote(query_key)
    city_code = hot_city[city_num].get("code", "100010000")
    industry = industry
    position = position
    page = 10 if page > 10 else page  # boss一般不超过10页

    start_url = "https://www.zhipin.com/job_detail/?query={}&city={}&industry={}&position={}".format(query_key_url,
                                                                                                     city_code,
                                                                                                     industry, position)

    file_name = u"{city}_{key}_{time}.csv".format(city=hot_city[city_num].get("name", ""), key=query_key,
                                                  time=datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    logger.info(u"-----------开始从BOSS直聘抓取：{}有关{}的职位, 取前{}页！".format(hot_city[city_num].get("name", ""), query_key, page))
    start_time = datetime.datetime.now()
    bsa = BossActions(finger_print=HEADERS, start_url=start_url, headless=True if headless == 0 else False)
    bsa.connect_chrome()
    jobs = bsa.search("", page=page)
    data2csv(jobs, file_name=file_name)
    logger.info("导出数据完成, 文件名：{}, 导出数据{}条".format(file_name, len(jobs)))
    run_time = round((datetime.datetime.now() - start_time).total_seconds() / 60.0, 2)
    logger.info(u"-----------完成从BOSS直聘抓取：{}有关{}的职位, 取前{}页, 共计数据{}条, 耗时:{}分钟".format(hot_city[city_num].get("name", ""),
                                                                                    query_key, page, len(jobs),
                                                                                    run_time))


def schedule_task():
    query_key = 'java'
    page = 10
    schedule.every().thursday.at("19:15").do(run_task,  query_key, 0, page)  # 传入参数
    schedule.every().thursday.at("20:35").do(run_task, query_key, 1, page)  # 传入参数
    schedule.every().thursday.at("22:25").do(run_task, query_key, 2, page)  # 传入参数
    schedule.every().thursday.at("23:55").do(run_task, query_key, 4, page)  # 传入参数
    schedule.every().thursday.at("01:55").do(run_task, query_key, 7, page)  # 传入参数
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    print("请使用以下命令启动chrome, 注意替换你电脑上chrome启动程序的路径：{}".format("/opt/google/chrome/chrome --remote-debugging-port=9222 --usr-data-dir='/home/charles/Desktop/123'"))
    while 1:
        query_key = input("请输入要查询的职位的关键字：")
        if not query_key:
            print("关键字不能为空")
        else:
            break
    city_num = int(input("请输入要查询的地域编号(0-全国,1-北京,2-上海, 3-广州, 4-深圳, 5-杭州,6-天津,7-西安,8-苏州,9-武汉,10-厦门,11-长沙,12-成都,13-郑州,14-重庆)："))
    page = int(input("需要抓取数据的总页码（每页30条, 不超过10页）："))
    page = 10 if page > 10 else page    #　boss一般不超过10页
    headless = 0 #int(input("是否显示浏览器(0-不显示, 1-显示)："))
    industry = ''
    position = ''
    run_task(query_key, city_num, page, industry, position, headless)



if __name__ == '__main__':
    main()
    # schedule_task()
