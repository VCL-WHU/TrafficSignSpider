# -*- coding: utf-8 -*-

import json

t_list = []

with open('url_list.txt','r') as ft:
    for data in ft.readlines():
        # print(data)
        t_list.append(data.strip())

with open("URL_LIST.json",'a') as fj:
    fj.write(json.dumps(t_list,indent = 4))

'''
print(t_list)
print(len(t_list))

'''
