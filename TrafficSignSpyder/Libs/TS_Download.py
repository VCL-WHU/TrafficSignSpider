# -*- coding: utf-8 -*-

import os
import requests

class ts_downloader():
    def __init__(self,make_folder_path='.',two_insideF = False):
        self.cur_Path = os.path.abspath(make_folder_path)
        self.is_two = two_insideF
        self.make_folders()

    def make_folders(self,make_folder_name = "Image"):

        target_path = self.cur_Path
        is_two = self.is_two

        #当前路径
        cur_path = os.path.abspath(target_path)

        #保存路径
        save_path = os.path.join(cur_path,make_folder_name)

        #这里创建文件夹路径，exist_ok=True 指如果有就不创建
        os.makedirs(save_path,exist_ok = True)

        if is_two:
            # confirm dir
            confirm_dir = os.path.join(save_path,'confirm_image')
            os.makedirs(confirm_dir,exist_ok = True)

            # doubt dir
            doubt_dir = os.path.join(save_path,'doubt_image')
            os.makedirs(doubt_dir,exist_ok = True)

        return None

    def start_download(self,url_list=[],lim_size = -1):

        if self.is_two == False:
            Download_path = os.path.join(self.cur_Path,'Image')
            self.Download_img(use_folder_name = Download_path,\
                              img_url_list = url_list,img_len = lim_size )
        return None

    def rename(self,start_num = 1):
        cur_path = os.path.abspath(self.cur_Path)
        path = os.path.join(cur_path,"Image")
        file_list = os.listdir(path)
        for i in range(len(file_list)):
            src_path = os.path.join(path,file_list[i])
            if os.path.exists(src_path):
                dst_path = os.path.join(path,str(start_num + i) + '.jpg')
                os.rename(src_path,dst_path)


    def Download_comfirm_img(self,func,c_path):
        pass

    def Download_doubt_img(self,func,d_path):
        pass


    def Download_img(self,use_folder_name,img_url_list,img_len):

        # print(len(img_url_list))

        if img_url_list is None or len(img_url_list) == 0:
            print("empty img url list")
            return None

        if img_len > len(img_url_list):
            img_len = len(img_url_list)

        for img_url in img_url_list[:img_len]:

            r = requests.get(img_url, stream=True)

            img_name = str(img_url).split('/')[-1]

            write_path = os.path.join(use_folder_name,img_name)

            with open(write_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=32):
                    f.write(chunk)

        return None

#---
