#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by charles on 2019-08-28
# Function: 

CITY_LIST = [
    {
        "code": 101010000,
        "name": "北京",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101010100,
                "name": "北京",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "beijing",
                "rank": 1
            }
        ],
        "firstChar": "b",
        "pinyin": None,
        "rank": 1
    },
    {
        "code": 101020000,
        "name": "上海",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101020100,
                "name": "上海",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shanghai",
                "rank": 1
            }
        ],
        "firstChar": "s",
        "pinyin": None,
        "rank": 9
    },
    {
        "code": 101030000,
        "name": "天津",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101030100,
                "name": "天津",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tianjin",
                "rank": 1
            }
        ],
        "firstChar": "t",
        "pinyin": None,
        "rank": 2
    },
    {
        "code": 101040000,
        "name": "重庆",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101040100,
                "name": "重庆",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "zhongqing",
                "rank": 2
            }
        ],
        "firstChar": "c",
        "pinyin": None,
        "rank": 22
    },
    {
        "code": 101050000,
        "name": "黑龙江",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101050100,
                "name": "哈尔滨",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "haerbin",
                "rank": 1
            },
            {
                "code": 101050200,
                "name": "齐齐哈尔",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qiqihaer",
                "rank": 2
            },
            {
                "code": 101050300,
                "name": "牡丹江",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "m",
                "pinyin": "mudanjiang",
                "rank": 10
            },
            {
                "code": 101050400,
                "name": "佳木斯",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jiamusi",
                "rank": 8
            },
            {
                "code": 101050500,
                "name": "绥化",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "suihua",
                "rank": 12
            },
            {
                "code": 101050600,
                "name": "黑河",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "heihe",
                "rank": 11
            },
            {
                "code": 101050700,
                "name": "伊春",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yichun",
                "rank": 7
            },
            {
                "code": 101050800,
                "name": "大庆",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "daqing",
                "rank": 6
            },
            {
                "code": 101050900,
                "name": "七台河",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qitaihe",
                "rank": 9
            },
            {
                "code": 101051000,
                "name": "鸡西",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jixi",
                "rank": 3
            },
            {
                "code": 101051100,
                "name": "鹤岗",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hegang",
                "rank": 4
            },
            {
                "code": 101051200,
                "name": "双鸭山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shuangyashan",
                "rank": 5
            },
            {
                "code": 101051300,
                "name": "大兴安岭",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "daxinganling",
                "rank": 13
            }
        ],
        "firstChar": "h",
        "pinyin": None,
        "rank": 8
    },
    {
        "code": 101060000,
        "name": "吉林",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101060100,
                "name": "长春",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "zhangchun",
                "rank": 1
            },
            {
                "code": 101060200,
                "name": "吉林",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jilin",
                "rank": 2
            },
            {
                "code": 101060300,
                "name": "四平",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "siping",
                "rank": 3
            },
            {
                "code": 101060400,
                "name": "通化",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tonghua",
                "rank": 5
            },
            {
                "code": 101060500,
                "name": "白城",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "baicheng",
                "rank": 8
            },
            {
                "code": 101060600,
                "name": "辽源",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "liaoyuan",
                "rank": 4
            },
            {
                "code": 101060700,
                "name": "松原",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "songyuan",
                "rank": 7
            },
            {
                "code": 101060800,
                "name": "白山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "baishan",
                "rank": 6
            },
            {
                "code": 101060900,
                "name": "延边",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yanbian",
                "rank": 9
            }
        ],
        "firstChar": "j",
        "pinyin": None,
        "rank": 7
    },
    {
        "code": 101070000,
        "name": "辽宁",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101070100,
                "name": "沈阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shenyang",
                "rank": 1
            },
            {
                "code": 101070200,
                "name": "大连",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dalian",
                "rank": 2
            },
            {
                "code": 101070300,
                "name": "鞍山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "a",
                "pinyin": "anshan",
                "rank": 3
            },
            {
                "code": 101070400,
                "name": "抚顺",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "f",
                "pinyin": "fushun",
                "rank": 4
            },
            {
                "code": 101070500,
                "name": "本溪",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "benxi",
                "rank": 5
            },
            {
                "code": 101070600,
                "name": "丹东",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dandong",
                "rank": 6
            },
            {
                "code": 101070700,
                "name": "锦州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jinzhou",
                "rank": 7
            },
            {
                "code": 101070800,
                "name": "营口",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yingkou",
                "rank": 8
            },
            {
                "code": 101070900,
                "name": "阜新",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "f",
                "pinyin": "fuxin",
                "rank": 9
            },
            {
                "code": 101071000,
                "name": "辽阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "liaoyang",
                "rank": 10
            },
            {
                "code": 101071100,
                "name": "铁岭",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tieling",
                "rank": 12
            },
            {
                "code": 101071200,
                "name": "朝阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "chaoyang",
                "rank": 13
            },
            {
                "code": 101071300,
                "name": "盘锦",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "p",
                "pinyin": "panjin",
                "rank": 11
            },
            {
                "code": 101071400,
                "name": "葫芦岛",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huludao",
                "rank": 14
            }
        ],
        "firstChar": "l",
        "pinyin": None,
        "rank": 6
    },
    {
        "code": 101080000,
        "name": "内蒙古",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101080100,
                "name": "呼和浩特",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huhehaote",
                "rank": 1
            },
            {
                "code": 101080200,
                "name": "包头",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "baotou",
                "rank": 2
            },
            {
                "code": 101080300,
                "name": "乌海",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wuhai",
                "rank": 3
            },
            {
                "code": 101080400,
                "name": "通辽",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tongliao",
                "rank": 5
            },
            {
                "code": 101080500,
                "name": "赤峰",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "chifeng",
                "rank": 4
            },
            {
                "code": 101080600,
                "name": "鄂尔多斯",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "e",
                "pinyin": "eerduosi",
                "rank": 6
            },
            {
                "code": 101080700,
                "name": "呼伦贝尔",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hulunbeier",
                "rank": 7
            },
            {
                "code": 101080800,
                "name": "巴彦淖尔",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "bayannaoer",
                "rank": 8
            },
            {
                "code": 101080900,
                "name": "乌兰察布",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wulanchabu",
                "rank": 9
            },
            {
                "code": 101081000,
                "name": "锡林郭勒",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xilinguole",
                "rank": 11
            },
            {
                "code": 101081100,
                "name": "兴安盟",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xinganmeng",
                "rank": 10
            },
            {
                "code": 101081200,
                "name": "阿拉善",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "a",
                "pinyin": "alashan",
                "rank": 12
            }
        ],
        "firstChar": "n",
        "pinyin": None,
        "rank": 5
    },
    {
        "code": 101090000,
        "name": "河北",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101090100,
                "name": "石家庄",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shijiazhuang",
                "rank": 1
            },
            {
                "code": 101090200,
                "name": "保定",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "baoding",
                "rank": 6
            },
            {
                "code": 101090300,
                "name": "张家口",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhangjiakou",
                "rank": 7
            },
            {
                "code": 101090400,
                "name": "承德",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "chengde",
                "rank": 8
            },
            {
                "code": 101090500,
                "name": "唐山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tangshan",
                "rank": 2
            },
            {
                "code": 101090600,
                "name": "廊坊",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "langfang",
                "rank": 10
            },
            {
                "code": 101090700,
                "name": "沧州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "cangzhou",
                "rank": 9
            },
            {
                "code": 101090800,
                "name": "衡水",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hengshui",
                "rank": 11
            },
            {
                "code": 101090900,
                "name": "邢台",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xingtai",
                "rank": 5
            },
            {
                "code": 101091000,
                "name": "邯郸",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "handan",
                "rank": 4
            },
            {
                "code": 101091100,
                "name": "秦皇岛",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qinhuangdao",
                "rank": 3
            }
        ],
        "firstChar": "h",
        "pinyin": None,
        "rank": 3
    },
    {
        "code": 101100000,
        "name": "山西",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101100100,
                "name": "太原",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "taiyuan",
                "rank": 1
            },
            {
                "code": 101100200,
                "name": "大同",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "datong",
                "rank": 2
            },
            {
                "code": 101100300,
                "name": "阳泉",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yangquan",
                "rank": 3
            },
            {
                "code": 101100400,
                "name": "晋中",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jinzhong",
                "rank": 7
            },
            {
                "code": 101100500,
                "name": "长治",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "zhangzhi",
                "rank": 4
            },
            {
                "code": 101100600,
                "name": "晋城",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jincheng",
                "rank": 5
            },
            {
                "code": 101100700,
                "name": "临汾",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "linfen",
                "rank": 10
            },
            {
                "code": 101100800,
                "name": "运城",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yuncheng",
                "rank": 8
            },
            {
                "code": 101100900,
                "name": "朔州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shuozhou",
                "rank": 6
            },
            {
                "code": 101101000,
                "name": "忻州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xinzhou",
                "rank": 9
            },
            {
                "code": 101101100,
                "name": "吕梁",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "lvliang",
                "rank": 11
            }
        ],
        "firstChar": "s",
        "pinyin": None,
        "rank": 4
    },
    {
        "code": 101110000,
        "name": "陕西",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101110100,
                "name": "西安",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xian",
                "rank": 1
            },
            {
                "code": 101110200,
                "name": "咸阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xianyang",
                "rank": 4
            },
            {
                "code": 101110300,
                "name": "延安",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yanan",
                "rank": 6
            },
            {
                "code": 101110400,
                "name": "榆林",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yulin",
                "rank": 8
            },
            {
                "code": 101110500,
                "name": "渭南",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "weinan",
                "rank": 5
            },
            {
                "code": 101110600,
                "name": "商洛",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shangluo",
                "rank": 10
            },
            {
                "code": 101110700,
                "name": "安康",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "a",
                "pinyin": "ankang",
                "rank": 9
            },
            {
                "code": 101110800,
                "name": "汉中",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hanzhong",
                "rank": 7
            },
            {
                "code": 101110900,
                "name": "宝鸡",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "baoji",
                "rank": 3
            },
            {
                "code": 101111000,
                "name": "铜川",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tongchuan",
                "rank": 2
            }
        ],
        "firstChar": "s",
        "pinyin": None,
        "rank": 27
    },
    {
        "code": 101120000,
        "name": "山东",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101120100,
                "name": "济南",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jinan",
                "rank": 1
            },
            {
                "code": 101120200,
                "name": "青岛",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qingdao",
                "rank": 2
            },
            {
                "code": 101120300,
                "name": "淄博",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zibo",
                "rank": 3
            },
            {
                "code": 101120400,
                "name": "德州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dezhou",
                "rank": 14
            },
            {
                "code": 101120500,
                "name": "烟台",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yantai",
                "rank": 6
            },
            {
                "code": 101120600,
                "name": "潍坊",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "weifang",
                "rank": 7
            },
            {
                "code": 101120700,
                "name": "济宁",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jining",
                "rank": 8
            },
            {
                "code": 101120800,
                "name": "泰安",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "taian",
                "rank": 9
            },
            {
                "code": 101120900,
                "name": "临沂",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "linyi",
                "rank": 13
            },
            {
                "code": 101121000,
                "name": "菏泽",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "heze",
                "rank": 17
            },
            {
                "code": 101121100,
                "name": "滨州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "binzhou",
                "rank": 16
            },
            {
                "code": 101121200,
                "name": "东营",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dongying",
                "rank": 5
            },
            {
                "code": 101121300,
                "name": "威海",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "weihai",
                "rank": 10
            },
            {
                "code": 101121400,
                "name": "枣庄",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zaozhuang",
                "rank": 4
            },
            {
                "code": 101121500,
                "name": "日照",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "r",
                "pinyin": "rizhao",
                "rank": 11
            },
            {
                "code": 101121700,
                "name": "聊城",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "liaocheng",
                "rank": 15
            }
        ],
        "firstChar": "s",
        "pinyin": None,
        "rank": 15
    },
    {
        "code": 101130000,
        "name": "新疆",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101130100,
                "name": "乌鲁木齐",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wulumuqi",
                "rank": 7
            },
            {
                "code": 101130200,
                "name": "克拉玛依",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "k",
                "pinyin": "kelamayi",
                "rank": 8
            },
            {
                "code": 101130300,
                "name": "昌吉",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "changji",
                "rank": 11
            },
            {
                "code": 101130400,
                "name": "巴音郭楞",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "bayinguoleng",
                "rank": 13
            },
            {
                "code": 101130500,
                "name": "博尔塔拉",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "boertala",
                "rank": 12
            },
            {
                "code": 101130600,
                "name": "伊犁",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yili",
                "rank": 18
            },
            {
                "code": 101130800,
                "name": "吐鲁番",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tulufan",
                "rank": 9
            },
            {
                "code": 101130900,
                "name": "哈密",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hami",
                "rank": 10
            },
            {
                "code": 101131000,
                "name": "阿克苏",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "a",
                "pinyin": "akesu",
                "rank": 14
            },
            {
                "code": 101131100,
                "name": "克孜勒苏柯尔克孜自治州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "k",
                "pinyin": "kezilesukeerkezi",
                "rank": 15
            },
            {
                "code": 101131200,
                "name": "喀什",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "k",
                "pinyin": "kashen",
                "rank": 16
            },
            {
                "code": 101131300,
                "name": "和田",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hetian",
                "rank": 17
            },
            {
                "code": 101131400,
                "name": "塔城",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tacheng",
                "rank": 19
            },
            {
                "code": 101131500,
                "name": "阿勒泰",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "a",
                "pinyin": "aletai",
                "rank": 20
            },
            {
                "code": 101131600,
                "name": "石河子",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shihezi",
                "rank": 5
            },
            {
                "code": 101131700,
                "name": "阿拉尔",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "a",
                "pinyin": "alaer",
                "rank": 1
            },
            {
                "code": 101131800,
                "name": "图木舒克",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tumushuke",
                "rank": 22
            },
            {
                "code": 101131900,
                "name": "五家渠",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wujiaqu",
                "rank": 23
            },
            {
                "code": 101132000,
                "name": "铁门关",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tiemenguan",
                "rank": 21
            },
            {
                "code": 101132100,
                "name": "北屯市",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "beitunshi",
                "rank": 2
            },
            {
                "code": 101132200,
                "name": "可克达拉市",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "k",
                "pinyin": "kekedalashi",
                "rank": 3
            },
            {
                "code": 101132300,
                "name": "昆玉市",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "k",
                "pinyin": "kunyushi",
                "rank": 4
            },
            {
                "code": 101132400,
                "name": "双河市",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shuangheshi",
                "rank": 6
            }
        ],
        "firstChar": "x",
        "pinyin": None,
        "rank": 31
    },
    {
        "code": 101150000,
        "name": "青海",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101150100,
                "name": "西宁",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xining",
                "rank": 1
            },
            {
                "code": 101150200,
                "name": "海东",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "haidong",
                "rank": 2
            },
            {
                "code": 101150300,
                "name": "海北",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "haibei",
                "rank": 3
            },
            {
                "code": 101150400,
                "name": "黄南",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huangnan",
                "rank": 4
            },
            {
                "code": 101150500,
                "name": "海南藏族自治州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hainan",
                "rank": 5
            },
            {
                "code": 101150600,
                "name": "果洛",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "g",
                "pinyin": "guoluo",
                "rank": 6
            },
            {
                "code": 101150700,
                "name": "玉树",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yushu",
                "rank": 7
            },
            {
                "code": 101150800,
                "name": "海西",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "haixi",
                "rank": 8
            }
        ],
        "firstChar": "q",
        "pinyin": None,
        "rank": 29
    },
    {
        "code": 101160000,
        "name": "甘肃",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101160100,
                "name": "兰州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "lanzhou",
                "rank": 1
            },
            {
                "code": 101160200,
                "name": "定西",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dingxi",
                "rank": 11
            },
            {
                "code": 101160300,
                "name": "平凉",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "p",
                "pinyin": "pingliang",
                "rank": 8
            },
            {
                "code": 101160400,
                "name": "庆阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qingyang",
                "rank": 10
            },
            {
                "code": 101160500,
                "name": "武威",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wuwei",
                "rank": 6
            },
            {
                "code": 101160600,
                "name": "金昌",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jinchang",
                "rank": 3
            },
            {
                "code": 101160700,
                "name": "张掖",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhangye",
                "rank": 7
            },
            {
                "code": 101160800,
                "name": "酒泉",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jiuquan",
                "rank": 9
            },
            {
                "code": 101160900,
                "name": "天水",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tianshui",
                "rank": 5
            },
            {
                "code": 101161000,
                "name": "白银",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "baiyin",
                "rank": 4
            },
            {
                "code": 101161100,
                "name": "陇南",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "longnan",
                "rank": 12
            },
            {
                "code": 101161200,
                "name": "嘉峪关",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jiayuguan",
                "rank": 2
            },
            {
                "code": 101161300,
                "name": "临夏",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "linxia",
                "rank": 13
            },
            {
                "code": 101161400,
                "name": "甘南",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "g",
                "pinyin": "gannan",
                "rank": 14
            }
        ],
        "firstChar": "g",
        "pinyin": None,
        "rank": 28
    },
    {
        "code": 101170000,
        "name": "宁夏",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101170100,
                "name": "银川",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yinchuan",
                "rank": 1
            },
            {
                "code": 101170200,
                "name": "石嘴山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shizuishan",
                "rank": 2
            },
            {
                "code": 101170300,
                "name": "吴忠",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wuzhong",
                "rank": 3
            },
            {
                "code": 101170400,
                "name": "固原",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "g",
                "pinyin": "guyuan",
                "rank": 4
            },
            {
                "code": 101170500,
                "name": "中卫",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhongwei",
                "rank": 5
            }
        ],
        "firstChar": "n",
        "pinyin": None,
        "rank": 30
    },
    {
        "code": 101180000,
        "name": "河南",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101180100,
                "name": "郑州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhengzhou",
                "rank": 1
            },
            {
                "code": 101180200,
                "name": "安阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "a",
                "pinyin": "anyang",
                "rank": 5
            },
            {
                "code": 101180300,
                "name": "新乡",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xinxiang",
                "rank": 7
            },
            {
                "code": 101180400,
                "name": "许昌",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xuchang",
                "rank": 10
            },
            {
                "code": 101180500,
                "name": "平顶山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "p",
                "pinyin": "pingdingshan",
                "rank": 4
            },
            {
                "code": 101180600,
                "name": "信阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xinyang",
                "rank": 15
            },
            {
                "code": 101180700,
                "name": "南阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "nanyang",
                "rank": 13
            },
            {
                "code": 101180800,
                "name": "开封",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "k",
                "pinyin": "kaifeng",
                "rank": 2
            },
            {
                "code": 101180900,
                "name": "洛阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "luoyang",
                "rank": 3
            },
            {
                "code": 101181000,
                "name": "商丘",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shangqiu",
                "rank": 14
            },
            {
                "code": 101181100,
                "name": "焦作",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jiaozuo",
                "rank": 8
            },
            {
                "code": 101181200,
                "name": "鹤壁",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hebi",
                "rank": 6
            },
            {
                "code": 101181300,
                "name": "濮阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "p",
                "pinyin": "puyang",
                "rank": 9
            },
            {
                "code": 101181400,
                "name": "周口",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhoukou",
                "rank": 16
            },
            {
                "code": 101181500,
                "name": "漯河",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "luohe",
                "rank": 11
            },
            {
                "code": 101181600,
                "name": "驻马店",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhumadian",
                "rank": 17
            },
            {
                "code": 101181700,
                "name": "三门峡",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "sanmenxia",
                "rank": 12
            },
            {
                "code": 101181800,
                "name": "济源",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jiyuan",
                "rank": 18
            }
        ],
        "firstChar": "h",
        "pinyin": None,
        "rank": 16
    },
    {
        "code": 101190000,
        "name": "江苏",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101190100,
                "name": "南京",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "nanjing",
                "rank": 1
            },
            {
                "code": 101190200,
                "name": "无锡",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wuxi",
                "rank": 2
            },
            {
                "code": 101190300,
                "name": "镇江",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhenjiang",
                "rank": 11
            },
            {
                "code": 101190400,
                "name": "苏州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "suzhou",
                "rank": 5
            },
            {
                "code": 101190500,
                "name": "南通",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "nantong",
                "rank": 6
            },
            {
                "code": 101190600,
                "name": "扬州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yangzhou",
                "rank": 10
            },
            {
                "code": 101190700,
                "name": "盐城",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yancheng",
                "rank": 9
            },
            {
                "code": 101190800,
                "name": "徐州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xuzhou",
                "rank": 3
            },
            {
                "code": 101190900,
                "name": "淮安",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huaian",
                "rank": 8
            },
            {
                "code": 101191000,
                "name": "连云港",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "lianyungang",
                "rank": 7
            },
            {
                "code": 101191100,
                "name": "常州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "changzhou",
                "rank": 5
            },
            {
                "code": 101191200,
                "name": "泰州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "taizhou",
                "rank": 12
            },
            {
                "code": 101191300,
                "name": "宿迁",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "suqian",
                "rank": 13
            }
        ],
        "firstChar": "j",
        "pinyin": None,
        "rank": 10
    },
    {
        "code": 101200000,
        "name": "湖北",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101200100,
                "name": "武汉",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wuhan",
                "rank": 1
            },
            {
                "code": 101200200,
                "name": "襄阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xiangyang",
                "rank": 5
            },
            {
                "code": 101200300,
                "name": "鄂州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "e",
                "pinyin": "ezhou",
                "rank": 6
            },
            {
                "code": 101200400,
                "name": "孝感",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xiaogan",
                "rank": 8
            },
            {
                "code": 101200500,
                "name": "黄冈",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huanggang",
                "rank": 10
            },
            {
                "code": 101200600,
                "name": "黄石",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huangshi",
                "rank": 2
            },
            {
                "code": 101200700,
                "name": "咸宁",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xianning",
                "rank": 11
            },
            {
                "code": 101200800,
                "name": "荆州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jingzhou",
                "rank": 9
            },
            {
                "code": 101200900,
                "name": "宜昌",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yichang",
                "rank": 4
            },
            {
                "code": 101201000,
                "name": "十堰",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shiyan",
                "rank": 3
            },
            {
                "code": 101201100,
                "name": "随州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "suizhou",
                "rank": 12
            },
            {
                "code": 101201200,
                "name": "荆门",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jingmen",
                "rank": 7
            },
            {
                "code": 101201300,
                "name": "恩施",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "e",
                "pinyin": "enshi",
                "rank": 13
            },
            {
                "code": 101201400,
                "name": "仙桃",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xiantao",
                "rank": 17
            },
            {
                "code": 101201500,
                "name": "潜江",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qianjiang",
                "rank": 14
            },
            {
                "code": 101201600,
                "name": "天门",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tianmen",
                "rank": 16
            },
            {
                "code": 101201700,
                "name": "神农架",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shennongjia",
                "rank": 15
            }
        ],
        "firstChar": "h",
        "pinyin": None,
        "rank": 17
    },
    {
        "code": 101210000,
        "name": "浙江",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101210100,
                "name": "杭州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hangzhou",
                "rank": 1
            },
            {
                "code": 101210200,
                "name": "湖州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huzhou",
                "rank": 5
            },
            {
                "code": 101210300,
                "name": "嘉兴",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jiaxing",
                "rank": 4
            },
            {
                "code": 101210400,
                "name": "宁波",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "ningbo",
                "rank": 2
            },
            {
                "code": 101210500,
                "name": "绍兴",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shaoxing",
                "rank": 6
            },
            {
                "code": 101210600,
                "name": "台州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "taizhou",
                "rank": 10
            },
            {
                "code": 101210700,
                "name": "温州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wenzhou",
                "rank": 3
            },
            {
                "code": 101210800,
                "name": "丽水",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "lishui",
                "rank": 11
            },
            {
                "code": 101210900,
                "name": "金华",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jinhua",
                "rank": 7
            },
            {
                "code": 101211000,
                "name": "衢州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "quzhou",
                "rank": 8
            },
            {
                "code": 101211100,
                "name": "舟山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhoushan",
                "rank": 9
            }
        ],
        "firstChar": "z",
        "pinyin": None,
        "rank": 11
    },
    {
        "code": 101220000,
        "name": "安徽",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101220100,
                "name": "合肥",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hefei",
                "rank": 1
            },
            {
                "code": 101220200,
                "name": "蚌埠",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "bangbu",
                "rank": 3
            },
            {
                "code": 101220300,
                "name": "芜湖",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wuhu",
                "rank": 2
            },
            {
                "code": 101220400,
                "name": "淮南",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huainan",
                "rank": 4
            },
            {
                "code": 101220500,
                "name": "马鞍山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "m",
                "pinyin": "maanshan",
                "rank": 5
            },
            {
                "code": 101220600,
                "name": "安庆",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "a",
                "pinyin": "anqing",
                "rank": 8
            },
            {
                "code": 101220700,
                "name": "宿州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "suzhou",
                "rank": 12
            },
            {
                "code": 101220800,
                "name": "阜阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "f",
                "pinyin": "fuyang",
                "rank": 11
            },
            {
                "code": 101220900,
                "name": "亳州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "bozhou",
                "rank": 14
            },
            {
                "code": 101221000,
                "name": "滁州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "chuzhou",
                "rank": 10
            },
            {
                "code": 101221100,
                "name": "淮北",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huaibei",
                "rank": 6
            },
            {
                "code": 101221200,
                "name": "铜陵",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tongling",
                "rank": 7
            },
            {
                "code": 101221300,
                "name": "宣城",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xuancheng",
                "rank": 16
            },
            {
                "code": 101221400,
                "name": "六安",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "liuan",
                "rank": 13
            },
            {
                "code": 101221500,
                "name": "池州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "chizhou",
                "rank": 15
            },
            {
                "code": 101221600,
                "name": "黄山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huangshan",
                "rank": 9
            }
        ],
        "firstChar": "a",
        "pinyin": None,
        "rank": 12
    },
    {
        "code": 101230000,
        "name": "福建",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101230100,
                "name": "福州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "f",
                "pinyin": "fuzhou",
                "rank": 1
            },
            {
                "code": 101230200,
                "name": "厦门",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "shamen",
                "rank": 2
            },
            {
                "code": 101230300,
                "name": "宁德",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "ningde",
                "rank": 9
            },
            {
                "code": 101230400,
                "name": "莆田",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "p",
                "pinyin": "putian",
                "rank": 3
            },
            {
                "code": 101230500,
                "name": "泉州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "quanzhou",
                "rank": 5
            },
            {
                "code": 101230600,
                "name": "漳州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhangzhou",
                "rank": 6
            },
            {
                "code": 101230700,
                "name": "龙岩",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "longyan",
                "rank": 8
            },
            {
                "code": 101230800,
                "name": "三明",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "sanming",
                "rank": 4
            },
            {
                "code": 101230900,
                "name": "南平",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "nanping",
                "rank": 7
            }
        ],
        "firstChar": "f",
        "pinyin": None,
        "rank": 13
    },
    {
        "code": 101240000,
        "name": "江西",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101240100,
                "name": "南昌",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "nanchang",
                "rank": 1
            },
            {
                "code": 101240200,
                "name": "九江",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jiujiang",
                "rank": 4
            },
            {
                "code": 101240300,
                "name": "上饶",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shangrao",
                "rank": 11
            },
            {
                "code": 101240400,
                "name": "抚州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "f",
                "pinyin": "fuzhou",
                "rank": 10
            },
            {
                "code": 101240500,
                "name": "宜春",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yichun",
                "rank": 9
            },
            {
                "code": 101240600,
                "name": "吉安",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jian",
                "rank": 8
            },
            {
                "code": 101240700,
                "name": "赣州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "g",
                "pinyin": "ganzhou",
                "rank": 7
            },
            {
                "code": 101240800,
                "name": "景德镇",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jingdezhen",
                "rank": 2
            },
            {
                "code": 101240900,
                "name": "萍乡",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "p",
                "pinyin": "pingxiang",
                "rank": 3
            },
            {
                "code": 101241000,
                "name": "新余",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xinyu",
                "rank": 5
            },
            {
                "code": 101241100,
                "name": "鹰潭",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yingtan",
                "rank": 6
            }
        ],
        "firstChar": "j",
        "pinyin": None,
        "rank": 14
    },
    {
        "code": 101250000,
        "name": "湖南",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101250100,
                "name": "长沙",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "zhangsha",
                "rank": 1
            },
            {
                "code": 101250200,
                "name": "湘潭",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xiangtan",
                "rank": 3
            },
            {
                "code": 101250300,
                "name": "株洲",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhuzhou",
                "rank": 2
            },
            {
                "code": 101250400,
                "name": "衡阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hengyang",
                "rank": 4
            },
            {
                "code": 101250500,
                "name": "郴州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "chenzhou",
                "rank": 10
            },
            {
                "code": 101250600,
                "name": "常德",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "changde",
                "rank": 7
            },
            {
                "code": 101250700,
                "name": "益阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yiyang",
                "rank": 9
            },
            {
                "code": 101250800,
                "name": "娄底",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "loudi",
                "rank": 13
            },
            {
                "code": 101250900,
                "name": "邵阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shaoyang",
                "rank": 5
            },
            {
                "code": 101251000,
                "name": "岳阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yueyang",
                "rank": 6
            },
            {
                "code": 101251100,
                "name": "张家界",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhangjiajie",
                "rank": 8
            },
            {
                "code": 101251200,
                "name": "怀化",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huaihua",
                "rank": 12
            },
            {
                "code": 101251300,
                "name": "永州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yongzhou",
                "rank": 11
            },
            {
                "code": 101251400,
                "name": "湘西",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xiangxi",
                "rank": 14
            }
        ],
        "firstChar": "h",
        "pinyin": None,
        "rank": 18
    },
    {
        "code": 101260000,
        "name": "贵州",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101260100,
                "name": "贵阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "g",
                "pinyin": "guiyang",
                "rank": 1
            },
            {
                "code": 101260200,
                "name": "遵义",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zunyi",
                "rank": 3
            },
            {
                "code": 101260300,
                "name": "安顺",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "a",
                "pinyin": "anshun",
                "rank": 4
            },
            {
                "code": 101260400,
                "name": "铜仁",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tongren",
                "rank": 6
            },
            {
                "code": 101260500,
                "name": "毕节",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "bijie",
                "rank": 5
            },
            {
                "code": 101260600,
                "name": "六盘水",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "liupanshui",
                "rank": 2
            },
            {
                "code": 101260700,
                "name": "黔东南",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qiandongnan",
                "rank": 8
            },
            {
                "code": 101260800,
                "name": "黔南",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qiannan",
                "rank": 9
            },
            {
                "code": 101260900,
                "name": "黔西南",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qianxinan",
                "rank": 7
            }
        ],
        "firstChar": "g",
        "pinyin": None,
        "rank": 24
    },
    {
        "code": 101270000,
        "name": "四川",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101270100,
                "name": "成都",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "chengdou",
                "rank": 1
            },
            {
                "code": 101270200,
                "name": "攀枝花",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "p",
                "pinyin": "panzhihua",
                "rank": 3
            },
            {
                "code": 101270300,
                "name": "自贡",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zigong",
                "rank": 2
            },
            {
                "code": 101270400,
                "name": "绵阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "m",
                "pinyin": "mianyang",
                "rank": 6
            },
            {
                "code": 101270500,
                "name": "南充",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "nanchong",
                "rank": 11
            },
            {
                "code": 101270600,
                "name": "达州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dazhou",
                "rank": 15
            },
            {
                "code": 101270700,
                "name": "遂宁",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "suining",
                "rank": 8
            },
            {
                "code": 101270800,
                "name": "广安",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "g",
                "pinyin": "guangan",
                "rank": 14
            },
            {
                "code": 101270900,
                "name": "巴中",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "bazhong",
                "rank": 17
            },
            {
                "code": 101271000,
                "name": "泸州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "luzhou",
                "rank": 4
            },
            {
                "code": 101271100,
                "name": "宜宾",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yibin",
                "rank": 13
            },
            {
                "code": 101271200,
                "name": "内江",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "neijiang",
                "rank": 9
            },
            {
                "code": 101271300,
                "name": "资阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "ziyang",
                "rank": 18
            },
            {
                "code": 101271400,
                "name": "乐山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "leshan",
                "rank": 10
            },
            {
                "code": 101271500,
                "name": "眉山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "m",
                "pinyin": "meishan",
                "rank": 12
            },
            {
                "code": 101271600,
                "name": "雅安",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yaan",
                "rank": 16
            },
            {
                "code": 101271700,
                "name": "德阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "deyang",
                "rank": 5
            },
            {
                "code": 101271800,
                "name": "广元",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "g",
                "pinyin": "guangyuan",
                "rank": 7
            },
            {
                "code": 101271900,
                "name": "阿坝",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "e",
                "pinyin": "aba",
                "rank": 19
            },
            {
                "code": 101272000,
                "name": "凉山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "liangshan",
                "rank": 21
            },
            {
                "code": 101272100,
                "name": "甘孜",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "g",
                "pinyin": "ganzi",
                "rank": 20
            }
        ],
        "firstChar": "s",
        "pinyin": None,
        "rank": 23
    },
    {
        "code": 101280000,
        "name": "广东",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101280100,
                "name": "广州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "g",
                "pinyin": "guangzhou",
                "rank": 1
            },
            {
                "code": 101280200,
                "name": "韶关",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shaoguan",
                "rank": 2
            },
            {
                "code": 101280300,
                "name": "惠州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "huizhou",
                "rank": 11
            },
            {
                "code": 101280400,
                "name": "梅州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "m",
                "pinyin": "meizhou",
                "rank": 12
            },
            {
                "code": 101280500,
                "name": "汕头",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shantou",
                "rank": 5
            },
            {
                "code": 101280600,
                "name": "深圳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shenzhen",
                "rank": 3
            },
            {
                "code": 101280700,
                "name": "珠海",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhuhai",
                "rank": 4
            },
            {
                "code": 101280800,
                "name": "佛山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "f",
                "pinyin": "foshan",
                "rank": 6
            },
            {
                "code": 101280900,
                "name": "肇庆",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhaoqing",
                "rank": 10
            },
            {
                "code": 101281000,
                "name": "湛江",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhanjiang",
                "rank": 8
            },
            {
                "code": 101281100,
                "name": "江门",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jiangmen",
                "rank": 7
            },
            {
                "code": 101281200,
                "name": "河源",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "heyuan",
                "rank": 14
            },
            {
                "code": 101281300,
                "name": "清远",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qingyuan",
                "rank": 16
            },
            {
                "code": 101281400,
                "name": "云浮",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yunfu",
                "rank": 21
            },
            {
                "code": 101281500,
                "name": "潮州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "chaozhou",
                "rank": 19
            },
            {
                "code": 101281600,
                "name": "东莞",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dongguan",
                "rank": 17
            },
            {
                "code": 101281700,
                "name": "中山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhongshan",
                "rank": 18
            },
            {
                "code": 101281800,
                "name": "阳江",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yangjiang",
                "rank": 15
            },
            {
                "code": 101281900,
                "name": "揭阳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "j",
                "pinyin": "jieyang",
                "rank": 20
            },
            {
                "code": 101282000,
                "name": "茂名",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "m",
                "pinyin": "maoming",
                "rank": 9
            },
            {
                "code": 101282100,
                "name": "汕尾",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shanwei",
                "rank": 13
            },
            {
                "code": 101282200,
                "name": "东沙群岛",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dongshaqundao",
                "rank": 22
            }
        ],
        "firstChar": "g",
        "pinyin": None,
        "rank": 19
    },
    {
        "code": 101290000,
        "name": "云南",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101290100,
                "name": "昆明",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "k",
                "pinyin": "kunming",
                "rank": 1
            },
            {
                "code": 101290200,
                "name": "曲靖",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qujing",
                "rank": 2
            },
            {
                "code": 101290300,
                "name": "保山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "baoshan",
                "rank": 4
            },
            {
                "code": 101290400,
                "name": "玉溪",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yuxi",
                "rank": 3
            },
            {
                "code": 101290500,
                "name": "普洱",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "p",
                "pinyin": "puer",
                "rank": 7
            },
            {
                "code": 101290700,
                "name": "昭通",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "z",
                "pinyin": "zhaotong",
                "rank": 5
            },
            {
                "code": 101290800,
                "name": "临沧",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "lincang",
                "rank": 8
            },
            {
                "code": 101290900,
                "name": "丽江",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "lijiang",
                "rank": 6
            },
            {
                "code": 101291000,
                "name": "西双版纳",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xishuangbanna",
                "rank": 12
            },
            {
                "code": 101291100,
                "name": "文山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wenshan",
                "rank": 11
            },
            {
                "code": 101291200,
                "name": "红河",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "honghe",
                "rank": 10
            },
            {
                "code": 101291300,
                "name": "德宏",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dehong",
                "rank": 14
            },
            {
                "code": 101291400,
                "name": "怒江",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "nujiang",
                "rank": 15
            },
            {
                "code": 101291500,
                "name": "迪庆",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "diqing",
                "rank": 16
            },
            {
                "code": 101291600,
                "name": "大理",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dali",
                "rank": 13
            },
            {
                "code": 101291700,
                "name": "楚雄",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "chuxiong",
                "rank": 9
            }
        ],
        "firstChar": "y",
        "pinyin": None,
        "rank": 25
    },
    {
        "code": 101300000,
        "name": "广西",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101300100,
                "name": "南宁",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "nanning",
                "rank": 1
            },
            {
                "code": 101300200,
                "name": "崇左",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "chongzuo",
                "rank": 14
            },
            {
                "code": 101300300,
                "name": "柳州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "liuzhou",
                "rank": 2
            },
            {
                "code": 101300400,
                "name": "来宾",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "laibin",
                "rank": 13
            },
            {
                "code": 101300500,
                "name": "桂林",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "g",
                "pinyin": "guilin",
                "rank": 3
            },
            {
                "code": 101300600,
                "name": "梧州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wuzhou",
                "rank": 4
            },
            {
                "code": 101300700,
                "name": "贺州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hezhou",
                "rank": 11
            },
            {
                "code": 101300800,
                "name": "贵港",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "g",
                "pinyin": "guigang",
                "rank": 8
            },
            {
                "code": 101300900,
                "name": "玉林",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "y",
                "pinyin": "yulin",
                "rank": 9
            },
            {
                "code": 101301000,
                "name": "百色",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "baise",
                "rank": 10
            },
            {
                "code": 101301100,
                "name": "钦州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qinzhou",
                "rank": 7
            },
            {
                "code": 101301200,
                "name": "河池",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "hechi",
                "rank": 12
            },
            {
                "code": 101301300,
                "name": "北海",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "beihai",
                "rank": 5
            },
            {
                "code": 101301400,
                "name": "防城港",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "f",
                "pinyin": "fangchenggang",
                "rank": 6
            }
        ],
        "firstChar": "g",
        "pinyin": None,
        "rank": 20
    },
    {
        "code": 101310000,
        "name": "海南",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101310100,
                "name": "海口",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "h",
                "pinyin": "haikou",
                "rank": 5
            },
            {
                "code": 101310200,
                "name": "三亚",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "sanya",
                "rank": 6
            },
            {
                "code": 101310300,
                "name": "三沙",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "sansha",
                "rank": 7
            },
            {
                "code": 101310400,
                "name": "儋州",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "danzhou",
                "rank": 8
            },
            {
                "code": 101310500,
                "name": "五指山",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wuzhishan",
                "rank": 19
            },
            {
                "code": 101310600,
                "name": "琼海",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qionghai",
                "rank": 14
            },
            {
                "code": 101310700,
                "name": "文昌",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wenchang",
                "rank": 18
            },
            {
                "code": 101310800,
                "name": "万宁",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "w",
                "pinyin": "wanning",
                "rank": 17
            },
            {
                "code": 101310900,
                "name": "东方",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dongfang",
                "rank": 10
            },
            {
                "code": 101311000,
                "name": "定安",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "d",
                "pinyin": "dingan",
                "rank": 9
            },
            {
                "code": 101311100,
                "name": "屯昌",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "tunchang",
                "rank": 16
            },
            {
                "code": 101311200,
                "name": "澄迈",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "chengmai",
                "rank": 4
            },
            {
                "code": 101311300,
                "name": "临高",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "lingao",
                "rank": 12
            },
            {
                "code": 101311400,
                "name": "白沙",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "baisha",
                "rank": 1
            },
            {
                "code": 101311500,
                "name": "昌江",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "changjiang",
                "rank": 3
            },
            {
                "code": 101311600,
                "name": "乐东",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "ledong",
                "rank": 11
            },
            {
                "code": 101311700,
                "name": "陵水",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "lingshui",
                "rank": 13
            },
            {
                "code": 101311800,
                "name": "保亭",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "b",
                "pinyin": "baoting",
                "rank": 2
            },
            {
                "code": 101311900,
                "name": "琼中",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "q",
                "pinyin": "qiongzhong",
                "rank": 15
            }
        ],
        "firstChar": "h",
        "pinyin": None,
        "rank": 21
    },
    {
        "code": 101340000,
        "name": "台湾",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101341100,
                "name": "台湾",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "t",
                "pinyin": "taiwan",
                "rank": 0
            }
        ],
        "firstChar": "t",
        "pinyin": None,
        "rank": 32
    },
    {
        "code": 101140000,
        "name": "西藏",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101140100,
                "name": "拉萨",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "lasa",
                "rank": 1
            },
            {
                "code": 101140200,
                "name": "日喀则",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "r",
                "pinyin": "rikaze",
                "rank": 2
            },
            {
                "code": 101140300,
                "name": "昌都",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "c",
                "pinyin": "changdou",
                "rank": 3
            },
            {
                "code": 101140400,
                "name": "林芝",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "l",
                "pinyin": "linzhi",
                "rank": 4
            },
            {
                "code": 101140500,
                "name": "山南",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "s",
                "pinyin": "shannan",
                "rank": 5
            },
            {
                "code": 101140600,
                "name": "那曲",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "n",
                "pinyin": "neiqu",
                "rank": 6
            },
            {
                "code": 101140700,
                "name": "阿里",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "a",
                "pinyin": "ali",
                "rank": 7
            }
        ],
        "firstChar": "x",
        "pinyin": None,
        "rank": 26
    },
    {
        "code": 101320000,
        "name": "香港",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101320300,
                "name": "香港",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "x",
                "pinyin": "xianggang",
                "rank": 0
            }
        ],
        "firstChar": "x",
        "pinyin": None,
        "rank": 33
    },
    {
        "code": 101330000,
        "name": "澳门",
        "tip": None,
        "subLevelModelList": [
            {
                "code": 101330100,
                "name": "澳门",
                "tip": None,
                "subLevelModelList": None,
                "firstChar": "a",
                "pinyin": "aomen",
                "rank": 0
            }
        ],
        "firstChar": "a",
        "pinyin": None,
        "rank": 34
    }
]
