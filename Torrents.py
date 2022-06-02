from unicodedata import category
from DB.DB import DB
from PTSites.PtSites import PtSites
import requests
import re
from lxml import etree
class Toreents(DB,PtSites):
    def __init__(self,site):
        self.site = self.PtSites[site]
        self.db = DB()

    def get_site_intro(self):
        return self.site['intro']

   


    def gen_search_url(self,keyword,**kwargs):
        #搜索种子
        baseurl = self.site['url'] + self.site['searchPage'] + keyword
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

    def get_page(self,url):
        #获取页面
        try:
            cookie = self.site['cookie']
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
                'Cookie': cookie
            }
            r = requests.get(url,headers=headers)
            r.encoding = 'utf-8'
            if r.status_code == 200:
                return r.text
            else :
                return None
        except:
            return None

    def test(self):
        print(self.site['siteMethod']['Category']())
    
a = Toreents('pttime')
a.test()
#print(a.get_torrent_id('https://www.pt.pt/torrent/detail/131'))
#a.gen_search_url('test',page=1,Category=[1,3,4])
#print(a.gen_torrent_page_url(page=1,Category=[1,3,4]))
#print(a.get_page(a.gen_search_url('test',page=1,Category=[1,3,4])))

