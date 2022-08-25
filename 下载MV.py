#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/12/17 19:23
# @Author  : huni
# @File    : QQ音乐MV.py
# @Software: PyCharm
# python 爬虫 selenium自动化爬取QQ音乐MV视频（解决动态加载的url）
# https://blog.csdn.net/m0_50944918/article/details/111367082?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166117201116781432947775%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166117201116781432947775&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-4-111367082-null-null.142^v42^pc_rank_34,185^v2^control&utm_term=python%E7%88%AC%E8%99%ABMV&spm=1018.2226.3001.4187
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
from time import sleep
from selenium.webdriver.common.by import By
import os
if __name__ == '__main__':
    # 实例化浏览器对象，传入浏览器驱动程序，运行之前用有界面的浏览器测试下
    # driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    # driver.maximize_window()
    # 无头浏览器
    option = webdriver.ChromeOptions()
    # 防止打印一些无用的日志
    option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(options=option)
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--disable-gpu')
    # 打开QQ音乐首页executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"
    driver.get('https://y.qq.com/')
    # 定义搜索关键词内容（这里用《可惜没如果》演示）也可以定义input输入
    key = '可惜没如果'
    # 找到搜索框,输入关键词
    sleep(16)
    search = driver.find_element(By.CLASS_NAME,'search_input__input').send_keys(key)
    
    # 找到搜索按钮并点击
    sleep(16)
    s_btn = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/button').click()
    # 如果出现提醒，关闭提醒
    sleep(16)
    try:
        warning = driver.find_element(By.XPATH,'//*[@id="divdialog_0"]/div[1]/a/i[1]').click()
    except:
        pass
    # 找到”MV“按钮并点击
    mvbtn = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/a[3]').click()
    sleep(30)
    # 获取页面源码
    html_source = driver.page_source
    # 解析html
    tree = etree.HTML(html_source)
    href = tree.xpath('//*[@id="mv_box"]/div/ul/li[1]/div/a/@href')[0]
    driver.get(href)
    sleep(20)
    # 获取mv页面源代码
    html_source1 = driver.page_source
    name = driver.title
    tree1 = etree.HTML(html_source1)
    src = tree1.xpath('//*[@id="video_player__source"]/@src')[0]
    driver.close()
    print(src)
    print(name)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    mp4_data = requests.get(url=src,headers=headers).content
    mp4_name = name.split('-')[0] + '-' + name.split('-')[1] + '.' + src.split('.')[-1]
    m_path = './MV音乐'
    if not os.path.exists(m_path):
        os.mkdir(m_path)
    mp4_path = m_path + f'/{mp4_name}'
    with open(mp4_path,'wb')as fp:
        fp.write(mp4_data)
        print(mp4_name,'下载完成')




