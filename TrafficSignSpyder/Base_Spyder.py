# -*- coding: utf-8 -*-


from Libs.TS_Request import ts_request
from Libs.TS_Download import ts_downloader
from Libs.TS_Re import ts_re
import json

class base_spyder():
    def __init__(self,the_url,limit_size = -1):
        self.start_url = the_url
        # print(self.start_url)
        self.ex_re = ts_re()

        self.ex_request = ts_request(url = self.start_url,
                                     demand_info = self.ex_re.make_small_dict_demand())
        self.ex_downloader = ts_downloader()

        self.image_url_list = []
        self.limit_size = limit_size

    def run(self):

        self.ex_request.run()
        self.image_url_list = self.ex_request.get_url_list()

        print(len(self.image_url_list))

        self.write_json(the_url_list = self.image_url_list)
        """
        self.ex_downloader.start_download(url_list=self.image_url_list,
                                         lim_size = self.limit_size)

        self.ex_downloader.rename()
        """
    def write_json(self, the_url_list):
        with open("URL_LIST.json",'w') as f:
            f.write(json.dumps(the_url_list,indent=4))

    def later_download(self,temp):
        pass