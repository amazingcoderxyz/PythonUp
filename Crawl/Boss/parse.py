#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by charles on 2019-08-28
# Function: 

import requests
from Crawl.config import HEADERS, str2cookies, logger, proxies
from bs4 import BeautifulSoup
from lxml import etree
import pprint
import pandas as pd
import datetime
import urllib.parse
import time

hot_city = [
    {
        "code": 100010000,
        "name": "全国",
    },
    {
        "code": 101010100,
        "name": "北京",
    },
    {
        "code": 101020100,
        "name": "上海",
    },
    {
        "code": 101280100,
        "name": "广州",
    },
    {
        "code": 101280600,
        "name": "深圳",
    },
    {
        "code": 101210100,
        "name": "杭州",
    },
    {
        "code": 101030100,
        "name": "天津",
    },
    {
        "code": 101110100,
        "name": "西安",
    },
    {
        "code": 101190400,
        "name": "苏州",
    },
    {
        "code": 101200100,
        "name": "武汉",
    },
    {
        "code": 101230200,
        "name": "厦门",
    },
    {
        "code": 101250100,
        "name": "长沙",
    },
    {
        "code": 101270100,
        "name": "成都",
    },
    {
        "code": 101180100,
        "name": "郑州",
    },
    {
        "code": 101040100,
        "name": "重庆",
    }
]

query_key = u"Python"
query_key = urllib.parse.quote(query_key)
city_code = "100010000"
industry = ""
position = ''

refer_url = "https://www.zhipin.com/job_detail/?query={}&city={}&industry={}&position={}".format(query_key, city_code, industry, position)

HEADERS["referer"] =refer_url
boss_cookies = "__c=1566958372; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1566958372; _uab_collina=156695837263691079001278; __l=l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.google.com%2F&friend_source=0&friend_source=0; lastCity={}; toUrl=https%3A%2F%2Fwww.zhipin.com%2F%2Fgongsi%2F38ac42a1bce530750XZ-2Nu5.html; JSESSIONID=""; __zp_stoken__=523egDZZFanBNaOZpHuUCw1DwJEtYJsahmHEvF0kK8rPgbxsWsqR2SF8bCPGKYHzVjq%2FdNaeTTHEjVDozDTNxkpuXw%3D%3D; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1567051699; __a=27247863.1566958372..1566958372.31.1.31.31".format(city_code)
# boss_cookies = "lastCity={}; __c=1566958372; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1566958372; _uab_collina=156695837263691079001278; __l=l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.google.com%2F&friend_source=0&friend_source=0; __zp_stoken__=395dHO%2F8dfwV9WotkzWD%2BOqR71ZroUuJBszemxrggTfQbrgnVKpXwc%2FTWyh8pql5xjr8gFYwRq55dgPFYxP62Q8E7g%3D%3D; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1566960953; __a=27247863.1566958372..1566958372.14.1.14.14"
boss_cookies.format(city_code)
cookies = str2cookies(boss_cookies)
# 101110100
HOST = "https://www.zhipin.com"
session = requests.session()
session.headers = HEADERS
session.proxies = proxies

def city_code_2_name(code):
    for it in hot_city:
        if it["code"] == int(code):
            return it['name']
    return str(code)


def parse_detail_page_by_html(html_text):
    detail = "unknown"
    team = "unknown"
    try:
        logger.info("parse_detail_page_by_html")
        html_text = html_text.replace("<!DOCTYPE html>", "<html>")
        detail_page = BeautifulSoup(html_text, 'lxml')
        sec = detail_page.find("div", {'class': 'job-sec'})
        detail_div = sec.find('div', {'class': 'text'})
        if detail_div:
            detail = detail_div.text.strip()

        team_div = detail_page.find("div", {'class': 'job-tags'})
        if team_div:
            team = team_div.text.strip()
    except Exception as e:
        logger.exception("e={}".format(e))

    return detail, team

def parse_detail_page_by_url(url):
    detail = "unknown"
    team = "unknown"
    try:
        logger.info("parse_detail_page_by_url, url={}".format(url))
        res = session.get(url)
        res.encoding = "utf-8"
        html_text = res.text.replace("<!DOCTYPE html>", "<html>")
        detail_page = BeautifulSoup(html_text, 'lxml')
        sec = detail_page.find("div", {'class': 'job-sec'})
        detail_div = sec.find('div', {'class': 'text'})
        if detail_div:
            detail = detail_div.text.strip()

        team_div = detail_page.find("div", {'class': 'job-tags'})
        if team_div:
            team = team_div.text.strip()
    except Exception as e:
        logger.exception("e={}".format(e))

    return detail, team



def data2csv(data_list, file_name=None):
    # 字典中的key值即为csv中列名
    dataframe = pd.DataFrame({'title': [data["title"] for data in data_list],
                              'money': [data["money"] for data in data_list],
                              'area': [data['area'] for data in data_list],
                              'experience': [data['experience'] for data in data_list],
                              'company_name': [data['company_name'] for data in data_list],
                              'company_industry': [data['company_industry'] for data in data_list],
                              'company_stage': [data['company_stage'] for data in data_list],
                              'company_scale': [data['company_scale'] for data in data_list],
                              'company_contact': [data['company_contact'] for data in data_list],
                              'job_description': [data['job_description'] for data in data_list],
                              'team_description': [data['team_description'] for data in data_list],
                              'detail_url': [data['detail_url'] for data in data_list],
                              'company_url': [data['company_url'] for data in data_list],
    })

    # 将DataFrame存储为csv,index表示是否显示行名，default=True
    time_str = datetime.datetime.now().strftime("%Y-%m-%d %H_%M_%S")
    if not file_name:
        file_name = "res_{}.csv".format(time_str)
    dataframe.to_csv(file_name)
    # dataframe.to_csv("{}_{}_{}_{}_{}.csv".format(city_code_2_name(city_code), query_key, industry, position, time_str), index=False, sep=',')


def parse_list_page(html_text, detail=True):
    jobs = []
    try:
        html_text = html_text.replace("<!DOCTYPE html>", "<html>")
        html = BeautifulSoup(html_text, "lxml")
        job_primarys = html.find_all("div", {"class": "job-primary"})
        for primary in job_primarys:
            try:
                if not primary:
                    logger.error("primary is None")
                    continue

                job_dict = {}
                job_info = primary.find("div", {'class': 'info-primary'})
                job_dict["title"] = job_info.find("div", {'class': "job-title"}).text
                job_dict['detail_url'] = '{}{}'.format(HOST, job_info.find("a").attrs.get("href", ''))

                if detail:
                    detail, team = parse_detail_page_by_url(job_dict['detail_url'])
                    job_dict['job_description'] = detail
                    job_dict['team_description'] = team
                else:
                    job_dict['job_description'] = ''
                    job_dict['team_description'] = ''

                job_dict['money'] = job_info.find("span", {'class': 'red'}).text
                pa = job_info.find("p")
                job_dict['area'] = str(pa.contents[0]).strip()
                job_dict['experience'] = str(pa.contents[2]).strip()
                if len(pa.contents) >= 5:
                    job_dict['education'] = str(pa.contents[4])
                else:
                    job_dict['education'] = 'unknown'

                company_info = primary.find("div", {'class': 'info-company'})
                ac = company_info.find('a')
                job_dict['company_url'] = '{}{}'.format(HOST, ac.attrs.get("href", ''))
                job_dict['company_name'] = ac.text

                pc = company_info.find('p')
                job_dict['company_industry'] = str(pc.contents[0])
                job_dict['company_stage'] = str(pc.contents[2])
                if len(pc.contents) >= 5:
                    job_dict['company_scale'] = str(pc.contents[4])
                else:
                    job_dict['company_scale'] = "unknown"


                publis_info = primary.find('div', {'class': 'info-publis'})
                job_dict['company_contact'] = publis_info.find('h3').text
                jobs.append(job_dict)
            except:
                continue

    except Exception as e:
        logger.exception("parse exception,e={}".format(e))

    return jobs


def main():
    res = session.get("https://www.zhipin.com/")
    res = session.get("https://www.zhipin.com/wapi/zpCommon/data/position.json")
    res = session.get("https://www.zhipin.com/wapi/zpCommon/data/city.json")
    res = session.get("https://www.zhipin.com/wapi/zpgeek/qrcode/generate.json?content=https%3A%2F%2Fwww.zhipin.com%2Fd%2Fv2%2F%3Ftype%3Dqr%26pkn%3Dmain-m%26sid%3Dmoren_14&w=200&h=200")

    for k, v in cookies.items():
        session.cookies[k] = v
    requst_url = "https://www.zhipin.com/job_detail/?query={}&city={}&industry={}&position={}".format(query_key, city_code, industry,
                                                                                         position)

    res = session.get(requst_url)

    page = 1
    jobs = []
    while res.status_code == 200 and page <= 20:
        try:
            page += 1
            res.encoding = "utf-8"
            html_text = res.text.replace("<!DOCTYPE html>", "<html>")
            html = BeautifulSoup(html_text, "lxml")
            job_primarys= html.find_all("div", {"class": "job-primary"})
            for primary in job_primarys:
                try:
                    if not primary:
                        logger.error("primary is None")
                        continue

                    job_dict = {}
                    job_info = primary.find("div", {'class': 'info-primary'})
                    job_dict["title"] = job_info.find("div", {'class': "job-title"}).text
                    job_dict['detail_url'] = '{}{}'.format(HOST, job_info.find("a").attrs.get("href", ''))

                    detail, team = parse_detail_page_by_url(job_dict['detail_url'])
                    job_dict['job_description'] = detail
                    job_dict['team_description'] = team
                    job_dict['money'] = job_info.find("span", {'class': 'red'}).text
                    pa = job_info.find("p")
                    job_dict['area'] = str(pa.contents[0]).strip()
                    job_dict['experience'] = str(pa.contents[2]).strip()
                    if len(pa.contents) >= 5:
                        job_dict['education'] = str(pa.contents[4])
                    else:
                        job_dict['education'] = 'unknown'

                    company_info = primary.find("div", {'class': 'info-company'})
                    ac = company_info.find('a')
                    job_dict['company_url'] = '{}{}'.format(HOST, ac.attrs.get("href", ''))
                    job_dict['company_name'] = ac.text

                    pc = company_info.find('p')
                    job_dict['company_industry'] = str(pc.contents[0])
                    job_dict['company_stage'] = str(pc.contents[2])
                    if len(pc.contents) >= 5:
                        job_dict['company_scale'] = str(pc.contents[4])
                    else:
                        job_dict['company_scale'] = "unknown"

                    publis_info = primary.find('div', {'class': 'info-publis'})
                    job_dict['company_contact'] = publis_info.find('h3').text
                    jobs.append(job_dict)
                except:
                    continue
            url = "https://www.zhipin.com/c{}/?query={}&page={}&ka=page-{}".format(city_code, query_key, page, page)
            logger.info("------fetch page={}".format(page))
            time.sleep(5)
            res = session.get(url)
        except Exception as e:
            logger.exception("parse exception,e={}".format(e))
            continue
    else:
        logger.error("request error: status code={}, text={}".format(res.status_code, res.text))

    print(len(jobs))
    pprint.pprint(jobs)
    data2csv(jobs)




if __name__ == '__main__':
    main()