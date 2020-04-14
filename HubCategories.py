from bs4 import BeautifulSoup
import requests

class HubCategories():

    def __init__(self):
        self.Prefix = 'https://www.pornhub.com'
        self.Target_url = [
            'https://www.pornhub.com/categories',#Popular
            'https://www.pornhub.com/categories?o=al',#Sort with letter
            'https://www.pornhub.com/categories?o=mv',#MostVideo
            'https://www.pornhub.com/gayporn',#GayPorn
        ]
# ----------------------------------------------------------------------------------------------
  #取得通用影片用
    def Get_Categories(self,List_Index):
        rs = requests.session()
        res = rs.get( self.Target_url[List_Index])
        soup = BeautifulSoup(res.text, 'html.parser')
        Total=''
        for index, data in enumerate(soup.select('ul.categories-list.videos.row-4-thumbs.js-mxpParent a.js-mxp')):
            if(index%2==0):
                Total+=(data['data-mxptext'])+'\n'
                Total+=(self.Prefix + data['href'])+'\n'
        return Total
# ----------------------------------------------------------------------------------------------
    #流行標籤
    def Get_Popular(self):
        return self.Get_Categories(0)
# ----------------------------------------------------------------------------------------------
    #流行標籤
    def Get_Sort_With_Letter(self):
        return self.Get_Categories(1)
# ----------------------------------------------------------------------------------------------
    #流行標籤
    def Get_MostVideo(self):
        return self.Get_Categories(2)
# ----------------------------------------------------------------------------------------------
    #男同性戀
    def Get_GayPorn(self):
        rs = requests.session()
        res = rs.get(self.Target_url[3])
        soup = BeautifulSoup(res.text, 'html.parser')
        Total=''
        for index, data in enumerate(soup.select('ul.nf-videos.videos.search-video-thumbs a.linkVideoThumb')):
            Total+=(data['title'])+'\n'
            Total+=(self.Prefix + data['href'])+'\n'
        return Total
# ----------------------------------------------------------------------------------------------