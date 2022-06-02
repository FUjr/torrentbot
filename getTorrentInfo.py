#import requests
#import json
from unicodedata import category
from ptSite import ptSite
from lxml import etree
import DB
import requests
import re

class getTorrentInfo(ptSite,DB) :
    def __init__(self,site):
        self.site = self.ptSites[site]
        self.db = DB(self.site[DATABASE])   
    def getSiteInfo(self):
        return self.site['intro']

    def getSearchCategory(self):
        return list(self.site['params']['Category'].keys())

    def getParamsDetail(self,param):
        return list(self.site['params'][param].keys())

    def getSupportParams4Users(self):
        #以中文的形式返回用户支持的参数
        return list(self.site['supportParams'].keys())

    def getSupportParams(self):
        #返回支持的参数列表（直接获取params中的key）
        return list(self.site['params'].keys())

    def genSearhUrl(self,keyword,**kwargs):
        parseurl = self.site['url'] + self.site['searchPage'] + keyword
        supportParams = self.getSupportParams()
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

    def getTorrentId(self,torrentDetailUrl):
        #获取种子id
        id = re.search(r'\d{1,}',torrentDetailUrl,)
        return id.group()

    def getTorrentList(self,pageUrl):
        #获取种子列表
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
            'cookie' : self.site['cookie']
        }
        r = requests.get(pageUrl,headers=headers)
        r.encoding = 'utf-8'
        res = r.text
        html = etree.HTML(res)
        torrentTitleList = html.xpath(self.site['XPATH']['titleXPATH'])
        torrentUrlList = html.xpath(self.site['XPATH']['urlXPATH'])
        torrentPromosionList = html.xpath(self.site['XPATH']['promosionXPATH'])
        torrentSizeList = html.xpath(self.site['XPATH']['sizeXPATH'])
        return torrentTitleList,torrentUrlList,res


        

DATABASE = 'PTBOT'
a = getTorrentInfo('pttime')

#res = a.getTorrentList(a.genSearhUrl('yyets',Category='电影'))
