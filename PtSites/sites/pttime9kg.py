from lxml import etree
import re
class pttime9kg():
    def __init__(self,sitedict):
        #初始化
        self.site = sitedict
        #获取pttime9kg相关信息

    def get_torrent_title_list(self,parsedhtml,index):
        #获取种子标题列表
        xpath = self.site['XPATH']['title'].replace("INDEX0",str(index))
        title = parsedhtml.xpath(xpath)
        if title == []:
            return ""
        else:
            return title[0]


    def get_torrent_size_list(self,parsedhtml,index):
        #获取种子大小列表
        xpath = self.site['XPATH']['size'].replace("INDEX0",str(index))
        size = parsedhtml.xpath(xpath)
        
        try:
            if size[1] == 'KB':
                size = float(size[0])/1024
                int(size)
            elif size[1] == 'MB':
                size = float(size[0])
                int(size)
            elif size[1] == 'GB':
                size = float(size[0]) * 1024
                int(size)
            elif size[1] == 'TB':
                size = float(size[0]) * 1024 * 1024
                int(size)
            else:
                print(size[1])
                size = int(size[0])
        except:
            size = 0

    
        return size


    def get_seeder_list(self,parsedhtml,index):
        #获取种子上传者列表
        xpath = self.site['XPATH']['seeder'].replace("INDEX0",str(index))
        seeder = parsedhtml.xpath(xpath)
        if seeder == []:
            print(index)
            print(xpath)
            return "0"
        else:
            return seeder[0]


    def get_leecher_list(self,parsedhtml,index):
        #获取种子下载者列表
        xpath = self.site['XPATH']['leecher'].replace("INDEX0",str(index))
        leecher = parsedhtml.xpath(xpath)
        if leecher == []:
            return "0"
        else:
            return leecher[0]


    def get_detail_url_list(self,parsedhtml,index):
        #获取种子详情页面列表
        xpath = self.site['XPATH']['detail'].replace("INDEX0",str(index))
        detail = parsedhtml.xpath(xpath)
        if detail == []:
            return ""
        else:
            return detail

    def get_id_List(self,parsedhtml,xpath):
        #获取种子id列表
        rex = r'(\d{1,})'
        detail = self.get_detail_url_list(parsedhtml,xpath)
        try :
            id = re.search(rex,detail[0]).group(1)
        except :
            id = ""
            print(detail)
        if id == None:
            return ""
        else:
            return id 

    def get_promosion_list(self,parsedhtml,index):
        #获取种子促销列表
        xpath = self.site['XPATH']['promosion'].replace("INDEX0",str(index))
        promosion = parsedhtml.xpath(xpath)
        if promosion == []:
            return ""
        else:
            return promosion[0]

          

    def get_category_list(self,parsedhtml,index):
        #获取种子类别列表
        rex_digit = r'\d{1,}'
        xpath = self.site['XPATH']['category'].replace("INDEX0",str(index))
        category = parsedhtml.xpath(xpath)
        if category == []:
            return ""
        else:
            try:
                category = re.search(rex_digit,category[0]).group(0)
                return category
            except:
                return ""


    def get_upload_timeStamp(self,parsedhtml,index):
        #获取种子上传时间
        xpath = self.site['XPATH']['timestamp'].replace("INDEX0",str(index))
        timestamp = parsedhtml.xpath(xpath)
        if timestamp == []:
            return "1970-01-01 08:00:00"
        else:
            return timestamp[0]

    def get_sub_title(self,parsedhtml,index):
        #获取种子子标题
        xpath = self.site['XPATH']['subtitle'].replace("INDEX0",str(index))
        subtitle = parsedhtml.xpath(xpath)
        
        if subtitle == []:
            return ""
        else:
            subtitle = "".join(subtitle)
            return subtitle

    def return_all_info(self,html,savetime):
        #获取种子信息
        parsedhtml = etree.HTML(html)
        torrentcount = self.get_group_count(parsedhtml)
        print(torrentcount)
        all_info_list = []
        for i in range(torrentcount):
            index = i + 2
            title = self.get_torrent_title_list(parsedhtml,index)
            size = self.get_torrent_size_list(parsedhtml,index)
            id = self.get_id_List(parsedhtml,index)
            seeder = self.get_seeder_list(parsedhtml,index)
            leecher = self.get_leecher_list(parsedhtml,index)
            timestamp = self.get_upload_timeStamp(parsedhtml,index)
            promosion = self.get_promosion_list(parsedhtml,index)
            category = self.get_category_list(parsedhtml,index)
            subtitle = self.get_sub_title(parsedhtml,index)
            all_info = {
                "title": title,
                "size": size,
                "id": id,
                "seeder": seeder,
                "leecher": leecher,
                "timestamp": timestamp,
                "promosion": promosion,
                "category" : category,
                "subtitle" : subtitle,
                "savetime" : savetime
            }

            
            all_info_list.append(all_info)
        return all_info_list

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

    def get_group_count(self,parsedhtml):
        #获取种子数量
        XPATH = '//table[@class="torrents"]/tr'
        res = parsedhtml.xpath(XPATH)
        return len(res) - 1

    def get_table_format(self):
        return self.site['storeType']

    def test(self):
        print(self.site)
        return 'testpass'

