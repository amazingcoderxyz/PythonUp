#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by charles on 2019-09-03
# Function: 

import pandas as pd
import numpy as np
import jieba
from collections import Counter
from wordcloud import WordCloud

# f = open(u'txt/AliceEN.txt','r').read()

import os
os.environ['FONT_PATH'] = '/home/charles/Code/PythonUp/Crawl/Boss/HYQiHei-25J.ttf'

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)

stopword_file = "stopwords.dat"
word_list = ["学信网", '统招', '二本或者以上学历', '两年以上相关工作经验', '二本以上学历', '私有云', '公有云', '微服务', '分布式', '本四硕三']
for wd in word_list:
    jieba.add_word(wd)

def read_file(file_name):
    fp = open(file_name, "r", encoding="utf-8")
    content_lines = fp.readlines()
    fp.close()
    #去除行末的换行符，否则会在停用词匹配的过程中产生干扰
    for i in range(len(content_lines)):
        content_lines[i] = content_lines[i].rstrip("\n")
    return content_lines


#剔除停用词
def cut_and_delete_stopwords(lines):
    stopwords = read_file(stopword_file)
    stopwords.append(' ')
    stopwords.append('\xa0')
    all_words = []

    for line in lines:
        all_words += [word for word in jieba.cut(line) if word not in stopwords]

    return all_words

def transfer_money(money_str):
    flag = 12
    avg_money_year = -1
    if money_str.endswith("/天"):
        avg_money_year = np.nan
    else:
        res = money_str.split("·")
        range_money = res[0][0:-1].split('-')
        avg_money_year = (int(range_money[0])+int(range_money[1]))/2
        flag = 12
        if len(res) > 1:
            flag = int(res[1][:-1])
        avg_money_year *= flag
    print("{}--{}-->{}".format(money_str, flag, avg_money_year))
    return avg_money_year

def parse_csv(file_name):
    print("开始解析：{}".format(file_name))
    df = pd.read_csv(file_name)

    titles = []
    for title in df['title'].items():
        titles.append(title[1])

    print(df["title"].value_counts())
    print(df["money"].value_counts())
    df['money_year'] = df['money'].map(transfer_money)
    print("年薪最低：%.2f万"%(df['money_year'].min()/10))
    print("年薪最高：%.2f万" %(df['money_year'].max() / 10))
    print("年薪平均：%.2f万" %(df['money_year'].mean() / 10))
    print("年薪中位数：%.2f万" %(df['money_year'].median() / 10))
    # all_des_word = []
    # for des in df["job_description"]:
    #     seg_list = jieba.cut(des, cut_all=False, HMM=True)
    #     all_des_word += seg_list

    all_words = cut_and_delete_stopwords(df["job_description"])

    dict_words = dict(Counter(all_words))
    res = sorted(dict_words.items(), key=lambda it: it[1], reverse=True)
    print(res)

    # wordcloud = WordCloud(background_color="white", width=1000, height=860, margin=2).generate(" ".join(all_words))
    wordcloud = WordCloud(background_color="white", font_path=os.environ['FONT_PATH'], width=1000, height=860, margin=2).generate_from_frequencies(dict_words)
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    wordcloud.to_file('test.png')



if __name__ == '__main__':
    file_name = u"西安_产品经理_20190905185114.csv"
    parse_csv(file_name)
    # transfer_money("20-40K")