from lxml import etree
import re
from pymysql import Timestamp
import requests
import time

from parso import parse
class haidan:
    def __init__(self,sitedict):
        #初始化
        self.site = sitedict
        #获取haidan相关信息


    def get_group_count(self,parsedhtml):
        #获取种子数量
        XPATH = '//div[@class="torrent_group"]'
        res = parsedhtml.xpath(XPATH)
        return len(res)

    def get_torrent_count(self,index,parsedhtml):
        XPATH = "//div[@class='torrent_group'][%s]//div[@class='torrent_item']" % index
        res = parsedhtml.xpath(XPATH)
        return len(res)



    def return_all_info(self,html,savetime):
        parsedhtml = etree.HTML(html)
        torrentNum = self.get_group_count(parsedhtml)
        torrent_info_list = []
        
        for i in range(torrentNum):
            index0 = i + 1
            itemNum = self.get_torrent_count(index0,parsedhtml)
            for j in range(itemNum):
                index1 = j + 1
                title = self.get_torrent_title(parsedhtml,index0)
                id = self.get_torrent_id(parsedhtml,index0,index1)
                size = self.get_torrent_size(parsedhtml,index0,index1)
                seeder = self.get_torrent_seeder(parsedhtml,index0,index1)
                leecher = self.get_torrent_leecher(parsedhtml,index0,index1)
                episode = self.get_torrent_episode(parsedhtml,index0,index1)
                timestamp = self.get_torrent_time(parsedhtml,index0,index1)
                category = self.get_torrent_category(parsedhtml,index0)
                all_info = {
                    'title':title,
                    'id':id,
                    'size':size,
                    'seeder':seeder,
                    'leecher':leecher,
                    'episode':episode,
                    'timestamp':timestamp,
                    'category':category,
                    'savetime' : savetime
                }
                torrent_info_list.append(all_info)
        return torrent_info_list


    def convert_torrent_id(self,url):
        rex = r'.*torrent_id=(\d{2,5})'
        id = re.search(rex,url).group(1)
        return id

    def get_torrent_id(self,parsedhtml,index0,index1):
        detail = self.get_torrent_detail(parsedhtml,index0,index1)
        id = self.convert_torrent_id(detail)
        return id

    def get_torrent_title(self,parsedhtml,index0):
        XPATH = self.site['XPATH']['title']
        XPATH = XPATH.replace('INDEX0',str(index0))
        title = parsedhtml.xpath(XPATH)
        longest_len = 0
        longest_title = ""
        for i in title:
             if len(i) > longest_len:
                    longest_len = len(i)
                    longest_title = i
        return longest_title

    def get_torrent_category(self,parsedhtml,index0):
        XPATH = self.site['XPATH']['category']
        XPATH = XPATH.replace('INDEX0',str(index0))
        category = parsedhtml.xpath(XPATH)
        rex = r'(\d{1,})'
        category = re.search(rex,category[0]).group(1)

        return category

    def get_torrent_detail(self,parsedhtml,index0,index1):
        XPATH = self.site['XPATH']['detail']
        
        XPATH = XPATH.replace('INDEX0',str(index0))
        XPATH = XPATH.replace('INDEX1',str(index1))
        detail = parsedhtml.xpath(XPATH)
        try:
            detail = detail[0]
        except:
            pass
        return detail

    def get_torrent_size(self,parsedhtml,index0,index1):
        XPATH = self.site['XPATH']['size']
        XPATH = XPATH.replace('INDEX0',str(index0))
        XPATH = XPATH.replace('INDEX1',str(index1))
        size = parsedhtml.xpath(XPATH)
        try :
            size = size[0]
            #转换为MB
            if 'MB' in size:
                size = float(size.replace('MB',''))
                size = size 
                size = round(size,2)

            #转换为GB
            elif 'GB' in size:
                size = float(size.replace('GB',''))
                size = size * 1024
                size = round(size,2)

            #转换为TB
            elif 'TB' in size:
                size = float(size.replace('TB',''))
                size = size * 1024 * 1024
                size = round(size,2)
            elif 'KB' in size:
                size = float(size.replace('KB',''))
                size = size / 1024
                size = round(size,2)
            else:
                rex_digital_only = r'(\d{1,})'
                size = re.search(rex_digital_only,size).group(1)

        except:
            size = ""

        return size
    
    def get_torrent_seeder(self,parsedhtml,index0,index1):
        XPATH = self.site['XPATH']['seeder']
        XPATH = XPATH.replace('INDEX0',str(index0))
        XPATH = XPATH.replace('INDEX1',str(index1))
        seeder = parsedhtml.xpath(XPATH)
        try :
            seeder = seeder[0]
        except:
            seeder = ""
        return seeder

    def get_torrent_leecher(self,parsedhtml,index0,index1):
        XPATH = self.site['XPATH']['leecher']
        XPATH = XPATH.replace('INDEX0',str(index0))
        XPATH = XPATH.replace('INDEX1',str(index1))
        leecher = parsedhtml.xpath(XPATH)
        try :
            leecher = leecher[0]
        except:
            leecher = ""

        return leecher
    
    def get_torrent_episode(self,parsedhtml,index0,index1):
        XPATH = self.site['XPATH']['episode']
        XPATH = XPATH.replace('INDEX0',str(index0))
        XPATH = XPATH.replace('INDEX1',str(index1))
        episode = parsedhtml.xpath(XPATH)
        try :
            episode = episode[0]
        except:
            episode = ""
        return episode

    def get_torrent_time(self,parsedhtml,index0,index1):
        XPATH = self.site['XPATH']['timestamp']
        XPATH = XPATH.replace('INDEX0',str(index0))
        XPATH = XPATH.replace('INDEX1',str(index1))
        time = parsedhtml.xpath(XPATH)
        try :
            time = time[0]
        except:
            time = ""
        return time

    def get_table_format(self):
        return self.site['storeType']

    def get_suppoert_params(self):
        #返回支持的参数列表（直接获取params中的key）
        return list(self.site['params'].keys())

    def gen_search_url(self,keyword,**kwargs):
        parseurl = self.site['url'] + self.site['searchPage'] + keyword
        supportParams = self.get_suppoert_params()
        if 'page' in kwargs:
            page = kwargs['page']
        else:
            page = 0
        parseurl = parseurl + self.site['params']['Page']['default'] + str(page)
        del supportParams[supportParams.index('Page')]
        #获取支持的参数
        for param in kwargs:
            if param in supportParams:
                #若支持的参数在支持的参数列表中，则添加到url中
                if isinstance(kwargs[param],list):
                    for item in kwargs[param]:
                    #若是列表，则遍历列表，添加到url中
                        if isinstance(item,int):
                        #若参数是整数，则按照索引值添转换成字符串
                            try:
                                item=list(self.site['params'][param].keys())[item]
                            except:
                                #若索引值超出范围，则跳过
                                continue
                        try:
                            parseurl += self.site['params'][param][item]
                            try:
                                del supportParams[supportParams.index(param)]
                            except ValueError:
                                pass
                            #若添加成功，则删除该参数
                        except KeyError:
                            print('KeyError:',param,item)        
                else:
                    parseurl += self.site['params'][param][kwargs[param]]
        for item in supportParams:
            #若支持的参数不在支持的参数列表中，则添加默认参数
            parseurl += self.site['params'][item]['default']
        return parseurl

    def get_site_intro(self):
        return self.site['intro']

    def gen_torrent_page_url(self,**kwargs):
        #生成默认的页面url
        baseurl = self.site['url'] + self.site['torrentListPage']
        supportParams = list(self.site['params'])
        if 'page' in kwargs:
            page = kwargs['page']
        else:
            page = 0
        baseurl = baseurl + self.site['params']['Page']['default'] + str(page)
        del supportParams[supportParams.index('Page')]
        #获取支持的参数
        for param in kwargs:
            if param in supportParams:
                if isinstance(kwargs[param],list):
                    #若参数是一个列表，则遍历列表，添加到url中
                    for item in kwargs[param]:
                        if isinstance(item,int):
                            try:
                                item=list(self.site['params'][param].keys())[item]
                            except:
                                continue
                        try:
                            baseurl += self.site['params'][param][item]
                            try:
                                del supportParams[supportParams.index(param)]
                            except ValueError:
                                pass
                        except KeyError:
                            print('KeyError:',param,item)
                else:
                    if isinstance(kwargs[param],int):
                        try:
                            kwargs[param]=list(self.site['params'][param].keys())[kwargs[param]]
                        except:
                            continue
                    baseurl += self.site['params'][param][kwargs[param]]
        for i in supportParams:
            baseurl += self.site['params'][i]['default']
        return baseurl

    def get_table_format(self):
        return self.site['storeType']

    def test(self):
        print(self.site)
        return 'testpass'