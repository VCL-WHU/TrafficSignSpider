# -*- coding: utf-8 -*-

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class ParamError(BaseException):
    pass


class ts_request():

    __doc__ = ""

    def __init__(self,url,demand_info):
        self.demand = demand_info

        self.start_url = url
        # self.url_pool = []
        self.url_list = []

        # print("ts init")
        # print(self.start_url)
    def get_soup(self,url,isJS = True):
        # print("IN ts_request")
        # print(url)
        # print(url == None)
        # url = self.start_url
        # url="http://soso.huitu.com/search?kw=%E4%BA%A4%E9%80%9A%E6%A0%87%E5%BF%97&page=1"
        if isJS:
            html = self.get_html(one_url = url,isroll = True,sbutton = "more-outer")
        else:
            html = requests.get(url).text
        # print(html)
        soup = BeautifulSoup(html,features = 'lxml')
        return soup

    def filter_html_label(self,theSoup):
        self.url_list = []
        # print(len(self.demand))
        if isinstance(self.demand,list):
            for demand_item in self.demand:
                find_list = theSoup.find_all(demand_item)
                if len(find_list) != 0:
                    for find_item in find_list:
                        try:
                            self.url_list.append(find_item['src'])
                        except KeyError as e:
                            pass
                        try:
                            self.url_list.append(find_item['_src'])
                        except KeyError as e:
                            pass

        elif isinstance(self.demand,dict):
            for demand_key in self.demand:
                for the_item in self.demand[demand_key]:
                    find_list = theSoup.find_all(demand_key,the_item)
                    if len(find_list) != 0:
                        for find_item in find_list:
                            try:
                                self.url_list.append(find_item['src'])
                            except KeyError as e:
                                pass
                            try:
                                self.url_list.append(find_item['_src'])
                            except KeyError as e:
                                pass

        else:
            # raise ParamError("demand wrong")
            print("demand wrong!")

        # print(self.url_list)
        del find_list
        return None

    def get_html(self, one_url,isroll = False,sbutton = None):

        driver = webdriver.Chrome()
        driver.get(one_url)
        # roll and click
        if isroll:
            for i in range(3):
                # print(i)
                try:
                    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                except Exception as e:
                    pass
                finally:
                    try:
                        driver.find_element_by_id(sbutton).click()
                    except Exception as e:
                        pass
                    finally:
                        time.sleep(1)

        # print("sleep")
        time.sleep(10)
        html = driver.page_source
        driver.quit()
        return html

    def run(self):
        start_soup = self.get_soup(url = self.start_url)
        self.filter_html_label(start_soup)

    def get_url_list(self):
        return self.url_list
    '''
    def find_Html_Url(self,params):
        pass

    def find_Image_Url(self,params):
        pass
    '''
