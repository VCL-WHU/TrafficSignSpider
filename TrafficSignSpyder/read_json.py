# coding = utf-8

import json
from Libs.TS_Download import ts_downloader

with open("URL_LIST.json",'r') as f:
    data = json.load(f)

print(len(data))
print(type(data))

c_d = ts_downloader()
# c_d.start_download(url_list=data,lim_size = -1)

c_d.rename()

print("Done")