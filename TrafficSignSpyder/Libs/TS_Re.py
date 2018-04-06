# -*- coding: utf-8 -*-

import re

class ts_re():
    def __init__(self):
        self.re_list = [
                             re.compile('.*?\.jpg'),
                             ]

        self.target_label = ['a','img']

        self.target_attr = ['src','href']

        self.target_value = ['_blank']

        self.target_value.extend(self.re_list)

    def make_all_dict_demand(self):

        ret_demand = {}
        temp_dict = {}
        for t_label in self.target_label:
            ret_demand[t_label] = []
            for t_attr in self.target_attr:
                for t_value in self.target_value:
                    temp_dict[t_attr] = t_value
                    ret_demand[t_label].append(temp_dict)
                    temp_dict = {}

        return ret_demand

    def make_small_dict_demand(self):
        ret_demand = {'img':[{'src':re.compile('.*?\.jpg')}]}
        return ret_demand