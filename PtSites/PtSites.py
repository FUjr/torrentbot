import sys
if __name__ == '__main__':
    import Siteinfo
else:
    from . import Siteinfo

class PtSites:
    def __init__(self,sitename):
        self.sitename = sitename
        try:
            if __name__ == '__main__':
                __import__('sites.'+sitename)
                ptcalss = getattr(sys.modules['sites.'+sitename],sitename)
            else:
                from . import sites
                #调用了sites包下的$sitename,如果修改了包名，这里也要修改
                __import__('PtSites.sites.'+sitename)
                ptcalss = getattr(sys.modules['PtSites.sites.'+sitename],sitename)
            
            self.ptsite = ptcalss(Siteinfo.PtSites[sitename])

            
        except ImportError:
            print('No site named',sitename)
            sys.exit(1)

    def test(self):
        print(self.ptsite.test())

    def gen_search_url(self,keyword,**kwargs):
        return self.ptsite.gen_search_url(keyword,**kwargs)

    def gen_torrent_page_url(self,**kwargs):
        return self.ptsite.gen_torrent_page_url(**kwargs)

    def get_site_intro(self):
        return self.ptsite.get_site_intro()

    def get_table_format(self):
        return self.ptsite.get_table_format()

    def return_all_info(self,html,savetime):
        return self.ptsite.return_all_info(html,savetime)