from bs4 import BeautifulSoup
import requests

class HubStar():


    def __init__(self):
        self.Prefix='https://www.pornhub.com'
        self.Target_url = [
            'https://www.pornhub.com/pornstars',#Popular
            'https://www.pornhub.com/pornstars?o=t',#Hot
            'https://www.pornhub.com/pornstars?o=mv',#MostViewed
            'https://www.pornhub.com/pornstars?o=ms',#MostSub
            'https://www.pornhub.com/pornstars?o=a',#Search Name
            'https://www.pornhub.com/pornstars?o=nv',#MostVideo
            'https://www.pornhub.com/pornstars?gender=male'#MalePornStar
        ]


# ----------------------------------------------------------------------------------------------
    #取得通用影片用
    def Get_Star(self,List_Index):
        rs = requests.session()
        res = rs.get( self.Target_url[List_Index])
        soup = BeautifulSoup(res.text, 'html.parser')
        Total=''
        for index, data in enumerate(soup.select('div.pornstar_container a.title.js-mxp')):
            Total+=(data.string)+'\n'
            Total+=(self.Prefix + data['href'])+'\n'
        return Total

# ----------------------------------------------------------------------------------------------
    #取得最受歡迎的色情明星
    def Get_Popular(self):
        return self.Get_Star(0)
# ----------------------------------------------------------------------------------------------
    #取得最熱門的色情明星
    def Get_Hot(self):
        return self.Get_Star(1)
# ----------------------------------------------------------------------------------------------
    #取得最多觀看次數的色情明星
    def Get_MostViewed(self):
        return self.Get_Star(2)
# ----------------------------------------------------------------------------------------------
    #取得最多訂閱的色情明星
    def Get_MostSub(self):
        return self.Get_Star(3)
# ----------------------------------------------------------------------------------------------
    #用名字取得色情明星
    def Get_NameStar(self):
        return self.Get_Star(4)
# ----------------------------------------------------------------------------------------------
    #取得最多影片的
    def Get_MostVideo(self):
        return self.Get_Star(5)
# ----------------------------------------------------------------------------------------------
    #取得男性色情明星
    def Get_MalePornStar(self):
        return self.Get_Star(6)
# ----------------------------------------------------------------------------------------------