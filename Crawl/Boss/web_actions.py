#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by charles on 2019-08-30
# Function: 

import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
from Crawl.config import logger
from Crawl.Boss.parse import parse_list_page, parse_detail_page_by_url, data2csv, parse_detail_page_by_html

class WebActions:
    def __init__(self, finger_print={}, headless=False):
        """
        初始化
        :param finger_print: 指定浏览器指纹，包括devices/user-agent
        :param headless: 是否指定浏览为无头浏览器, 默认为False
        """
        self.device = finger_print.get("device", "")
        self.user_agent = finger_print.get("user_agent", "")
        if not self.user_agent:
            self.user_agent = finger_print.get("user-agent", "")
        self.headless = headless
        self.driver = None
        self.options = None

    def start_chrome(self, force_display=False, force_client=""):
        """
        配置并启动浏览器
        :param force_display: 强制显示chrome界面
        :param force_client: 强制指定启动chrome的环境， 可选输入项为"pc"或“mobile"
        :return: True/False
        """
        try:
            # 定制浏览器启动项
            chrome_options = webdriver.ChromeOptions()
            if self.headless and not force_display:
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--disable-extensions')
                chrome_options.add_argument('--disable-gpu')

            chrome_options.add_argument('--disable-infobars')
            chrome_options.add_argument('--disable-popup-blocking')  # 禁止弹出拦截
            chrome_options.add_argument("--ignore-certificate-errors")  # 忽略 Chrome 浏览器证书错误报警提示
            chrome_options.add_argument('lang=zh_cn')

            prefs = {'profile.default_content_setting_values':{'notifications': 2}}
            chrome_options.add_experimental_option('prefs', prefs)

            if self.user_agent and force_client != "mobile":
                chrome_options.add_argument('--user-agent={}'.format(self.user_agent))

            if self.device and force_client != "pc":
                # 移动设备仿真
                mobile_emulation = {
                    'deviceName': self.device
                    # "deviceMetrics": {"width": 600, "height":800, "pixelRatio": 4.0},
                    # "userAgent": "Mozilla/5.0 (Linux; Android 8.0.0; XT1635-02 Build/OPNS27.76-12-22-9)"
                }
                chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

            chrome_driver = webdriver.Chrome(chrome_options=chrome_options)
            time.sleep(1)

            logger.info("start_chrome device={}, user-agent={}, headless={}, options={}".format(self.device, self.user_agent,
                                                                                    self.headless, chrome_options.arguments))

            self.driver = chrome_driver
            self.options = chrome_options
            return True
        except Exception as e:
            logger.error("The browser did not start successfully, exception: {}".format(str(e)))
            return False

    def quit(self):
        if self.driver:
            self.driver.quit()

    def get_cookies(self, domain="zhipin"):
        cookies_list = []
        if self.driver:
            all_cookies = self.driver.get_cookies()
            if domain:
                for cookie in all_cookies:
                    if domain in cookie.get("domain", ""):
                        cookies_list.append(cookie)
            else:
                cookies_list = all_cookies

        return cookies_list

    def browse_page(self, browse_times=0, distance=0, interval=0, back_top=True):
        """
        浏览页面
        :param browse_times: 浏览次数
        :param distance: 每次间隔距离，默认为零，代表使用随机距离
        :param interval: 间隔时间， 单位秒, 默认为零，代表使用随机停顿时间
        :param back_top: 是否回到顶点
        :return:
        """
        # 浏览页面js
        try:
            logger.info('browse_page start.')
            y_dis = 0
            if browse_times <= 0:
                browse_times = random.randint(3, 15)

            for i in range(browse_times):
                if interval <= 0:
                    self.sleep(1, 10)
                else:
                    time.sleep(interval)

                if distance > 0:
                    y_dis += distance
                else:
                    y_dis += random.randint(20, 200)

                self.driver.execute_script("window.scrollTo(0,{})".format(y_dis))

            if back_top:
                self.driver.execute_script("window.scrollTo(0,0)")

            logger.info('browse_page end.')
            return True
        except Exception as e:
            logger.exception('browse_page exception. e={}'.format(e))
            return False

    def click(self, ele, double=False):
        """
        封装的复合点击函数
        :param ele:需要点击的元素
        :param double: 是否双击
        :return: 成功返回True, 失败返回false
        """
        if not ele:
            return False

        try:
            time.sleep(1)
            ele.click()
        except (WebDriverException, ElementNotVisibleException, ElementNotSelectableException,
                ElementClickInterceptedException, ElementNotInteractableException) as e:
            time.sleep(1)
            action = ActionChains(self.driver)
            if double:
                action.move_to_element(ele).double_click(ele)
            else:
                action.move_to_element(ele).click(ele)
            action.perform()
        return True

    def send_keys(self, ele, inputs, smart=True):
        """
        封装输入的函数
        :param ele: 需要输入的元素
        :param inputs: 传入的输入内容
        :param smart: 是否智能输入
        :return:
        """
        if not all([ele, inputs]):
            return False

        try:
            if smart:
                while inputs:
                    n = random.randint(2, 8)
                    if n > len(inputs):
                        n = len(inputs)
                    split_inputs = inputs[:n]
                    ele.send_keys(split_inputs)
                    self.sleep(0.2, 1.5)
                    inputs = inputs[n:]
            else:
                ele.send_keys(inputs)
        except Exception as e:
            logger.info("send_keys catch exception, e={}".format(e))
            return False

        return True

    def sleep(self, lower=2, upper=5):
        """
        随机休眠
        :param lower: 最短休眠时间
        :param upper: 最长休眠时间
        :return:
        """
        if lower > upper:
            tmp = lower
            lower = upper
            upper = tmp

        sleep_time = random.uniform(lower, upper)
        sleep_time = 1 if sleep_time <= 0 else sleep_time
        time.sleep(sleep_time)
        return True


class BossActions(WebActions):
    """
    BossActions 各种操作的基类, 封装通用的操作函数
    """
    def __init__(self, finger_print={},
                 headless=False, start_url="https://www.zhipin.com/", account_info={}):
        """
        初始化
        :param account_info: 账号相关的信息，如账号、密码、性别等，必须是字典类型
        :param finger_print: 指定浏览器指纹，包括devices/user-agent
        :param headless: 是否指定浏览为无头浏览器
        :param start_url: 启动的URL
        """
        assert isinstance(account_info, dict), "账号信息必须是字典类型"
        assert isinstance(finger_print, dict), "浏览器指纹"

        self.account = account_info.get("account", "")
        self.password = account_info.get("password", "")
        self.gender = account_info.get("gender", 1)
        self.phone_number = account_info.get("phone_number", "")
        self.cookies = account_info.get("configure", {}).get("cookies", "")
        self.start_url = start_url
        self.fb_exp = None
        super(BossActions, self).__init__(finger_print=finger_print, headless=headless)
        logger.info("BossActions init, account_info={}, device={}, user_agent={}, headless={}, "
                    "start_url={}".format(account_info, self.device, self.user_agent, headless, start_url))

    def search(self, keyword='', page=1):
        assert self.driver, "Driver is not valid! Please invoke start_chrome before login!"
        self.driver.get(self.start_url)
        self.sleep()
        all_jobs = []
        try:
            if keyword:
                query_box = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.NAME, 'query')))
                # email_box.send_keys(account)
                self.send_keys(query_box, keyword)
                self.sleep()
                query_box.send_keys(Keys.ENTER)
                self.sleep()

            start_page = 1
            while start_page <= page:
                logger.info("--------开始抓取第{}页".format(start_page))
                jobs = parse_list_page(self.driver.page_source, detail=False)
                # job_primarys = self.driver.find_elements_by_class_name("info-primary")
                index_in_page = 0
                list_page_url = self.driver.current_url     # 保留工作列表页面的链接, 详情抓取完成后再回到这个页面
                for jp in jobs:
                    index_in_page += 1
                    try:
                        detail_url = jp.get("detail_url", "")
                        if not detail_url:
                            continue
                        self.driver.get(detail_url)
                        self.sleep(1, 3)
                        logger.info("获取第{}页中第{}个工作职位详情,　职位标题：{}, 详情面URL={}".format(start_page, index_in_page, jp.get("title", ''), self.driver.current_url))
                        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'job-sec')))
                        jd, td = parse_detail_page_by_html(self.driver.page_source)
                        jp['job_description'] = jd
                        jp['team_description'] = td
                        self.sleep(1, 3)
                    except Exception as e:
                        logger.exception("遍历获取详情页数据时异常, 跳过该详情页解析! url={}, e={}".format(detail_url, e))
                        self.sleep(5, 15)   # 如果异常，在这里降降速
                        continue

                all_jobs += jobs
                logger.info("已获取{}页数据, 累计{}条".format(start_page, len(all_jobs)))

                if start_page >= page:
                    break

                self.driver.get(list_page_url)
                self.sleep()
                logger.info("回到工作列表页面：{}".format(self.driver.current_url))
                # 回到列表页面后，拉到最下面，进行翻页
                self.browse_page(browse_times=1, distance=3000, back_top=False)

                next_btn_disabled = self.driver.find_elements_by_class_name("next disabled")
                if next_btn_disabled:
                    logger.warning("已经到最后一页了, 下一页按钮处于禁用状态．next button is disabled. page={}".format(start_page))
                    break

                next_btn = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located((By.CLASS_NAME, 'next')))
                self.click(next_btn)
                self.sleep()
                start_page += 1
                logger.info("翻到第{}页, url={}".format(start_page, self.driver.current_url))
        except Exception as e:
            logger.exception("获取数据异常：{}".format(e))

        self.quit()
        return all_jobs

    def connect_chrome(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        if self.headless:
            chrome_options.add_argument('--headless')
        chrome_driver = webdriver.Chrome(chrome_options=chrome_options)
        print(chrome_driver.title)
        self.driver = chrome_driver
        self.options = chrome_options
        return True

"""/opt/google/chrome/chrome --remote-debugging-port=9222 --usr-data-dir="/home/charles/Desktop/123"
"""