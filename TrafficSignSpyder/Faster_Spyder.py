# -*- coding: utf-8 -*-

from Base_Spyder import base_spyder

class faster_spyder(base_spyder):
    def __init__(self,url,limit_size = -1):
        base_spyder.__init__(url,limit_size)
        
        self.isListEmpty = True

    def renew_signal(self):
        self.isListEmpty = (len(set(base_spyder.image_url_list))==0)
        return self.isListEmpty

    def run(self):
        base_spyder.run()
