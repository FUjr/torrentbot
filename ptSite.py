#该文件为pt详情文件
class ptSite:
    ptSites = {
        'btschool': {
            'intro' : 'bt学院，是一个大站。主要资源为电影资源，部分软件、音乐资源，无r18资源',
            'cookie' : 'c_secure_uid=NjU4NjI%3D; c_secure_pass=3c6f7f86fa472d6dc34025a073f32275; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D',
            'url' : 'https://pt.btschool.club/',
            'titleXPATH' : '//tbody/tr/td/table[@class="torrents"]/tbody/tr/td/table/tbody/tr/td/a/@title',
            'urlXPATH' : '//tbody/tr/td/table[@class="torrents"]/tbody/tr/td/table/tbody/tr/td/a/@href',
            'torrentListPage' : 'torrent.php?',
            'searchPage' : 'search.php?search='
        },

        'haidan' : {
            'intro' : '海胆，是一个小站。主要资源为电影资源，部分软件、音乐资源，无r18资源',
            'cookie' : '',
            'url' : 'https://haidan.video/'
        },
        'pttime' : {
            'intro' : 'pttime，是一个小站。主要资源为电影资源和r18资源，部分软件、音乐资源，特色是r18资源',
            'cookie' : 'c_secure_uid=NDcyNzI%3D; c_secure_pass=ac141922646c0bcea38a6132de5fe5aa; c_secure_ssl=eWVhaA%3D%3D; c_secure_tracker_ssl=eWVhaA%3D%3D; c_secure_login=bm9wZQ%3D%3D',
            'url' : 'https://www.pttime.org/',
            'XPATH':{
                'titleXPATH' : '//td[@class="embedded"]/a/b/text()',
                'urlXPATH' : '//table[@class="torrents"]//td[@class="embedded"]/a[@class="torrentname"]/@href',
                'promosionXPATH' : '//td[@class="embedded"]//a/font/text()',
                'sizeXPATH' : '//table[@class="torrents"]//tr/td[@class="rowfollow"][4]/text()',
                'seeder' : '//table[@class="torrents"]//tr/td[@class="rowfollow"][5]/text()',
                'leecher' : '//table[@class="torrents"]//tr/td[@class="rowfollow"][6]//text()',
                'pageListXPATH' : '/html/body/table/tbody/tr/td/table/tbody/tr/td/p[1]/a//text()',
            },
            'torrentListPage' : 'torrents.php?page=',
            'searchPage' : 'torrents.php?inclbookmarked=0&search=',
            'supportParams' : {
                #获取参数类型
                '类型' : 'Category',
                '促销模式' : 'Promotion', 
                '是否活种' : 'Incldead',
                '搜索范围' : 'SearchRange',
                '排序方式' : 'SortBy',
                '排序规则' : 'OrderBy',
                '页面' : 'Page',
            },
            'params':{
                'Category' :{
                    'default':'',
                    '电影' : '&cat401=1', 
                    '电视剧' : '&cat402=1',
                    '综艺' : '&cat403=1',
                    '纪录片' : '&cat404=1',
                    '体育' : '&cat405=1',
                    '游戏' : '&cat406=1',
                    '音乐' : '&cat408=1',
                    '曲艺' : '&cat409=1',
                    '技能' : '&cat411=1',
                    '考试' : '&cat412=1',
                    '书籍' : '&cat413=1',
                    '编程' : '&cat420=1',
                    '2.5次元' : '&cat430=1',
                    '二次元' : '&cat431=1',
                    '婴幼' : '&cat432=1',
                    '素材' : '&cat450=1',
                    '软件' : '&cat451=1',
                    '其他' : '&cat490=1'
                },
                'Promotion':{
                    'default':'&spstate=0',
                    '全部' : '&spstate=0',
                    '普通' : '&spstate=1',
                    '免费' : '&spstate=2',
                    '2X上传' : '&spstate=3',
                    '2X免费' : '&spstate=4',
                    '50%免费' : '&spstate=5',
                    '2X上传&50%免费' : '&spstate=6',
                    '30%免费' : '&spstate=7',
                    '0流量' : '&spstate=8',
                },
                'Incldead': {
                    'default':'&incldead=1',
                    'all' : '&incldead=0',
                    'alive' : '&incldead=1',
                    'dead' : '&incldead=2',
                },
                'SearchRange':{
                    'default':'&search_area=0',
                    '标题':'&search_area=0',
                    '简介':'&search_area=1',
                    '副标题' : '&search_area=2',
                    '发布者' : '&search_area=3',
                    'IMDb链接' : '&search_area=4',
                    '豆瓣链接或ID' : '&search_area=5',
                },
                'SortBy':{
                    'default':'&sort=4',
                    '发布时间' : '&sort=4',
                    '种子数' : '&sort=7',
                    '完成数' : '&sort=6',
                    '大小' : '&sort=5',
                    '下载数' : '&sort=8', 
                    'PTR' : '&sort=10', 
                },
                'OrderBy':{
                    'default':'&type=desc',
                    '降序' : '&type=desc',
                    '升序' : '&type=asc',
                },
                'Page':{
                    'default':'&page=',
                },
            },
            
        }
    }
    def __init__(self):
        pass

    def getSiteList(self):
        return list(self.ptSites.keys())

    def getSiteInfo(self, site):
        return self.ptSites[site]['intro']

    def getParamsCategroy(self, site):
        return list(self.ptSites[site]['paramsCategroy'].keys())
    

    


