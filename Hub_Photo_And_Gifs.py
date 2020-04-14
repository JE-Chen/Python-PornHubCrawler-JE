from bs4 import BeautifulSoup
import requests

class Hub_Photo_And_Gifs():

    def __init__(self):
        self.Prefix = 'https://www.pornhub.com'
        self.Target_url = [
            'https://www.pornhub.com/gifs',#Gifs
            'https://www.pornhub.com/albums/female-straight',#Album All
            'https://www.pornhub.com/albums/female-straight?o=tr',#Album MonthTopRated
        ]
# ----------------------------------------------------------------------------------------------
    #取得本月推薦的Gif
    def Get_Month_TopRated(self):
        rs = requests.session()
        res = rs.get(self.Target_url[0])
        soup = BeautifulSoup(res.text, 'html.parser')

        Title_List = []
        Link_List = []

        Total=''
        for index, data in enumerate(soup.select('div.container li.gifVideoBlock a span.title')):
            Title_List.append(data.string)

        for index, data in enumerate(soup.select('div.container li.gifVideoBlock a')):
            Link_List.append(self.Prefix + data['href'])

        for index in range(len(Title_List)):
            Total+=(Title_List[index])+'\n'
            Total+=(Link_List[index])+'\n'
        return Total
# ----------------------------------------------------------------------------------------------
    #取得Gif Tag 連結
    def Get_Gif_Tags(self):
        rs = requests.session()
        res = rs.get(self.Target_url[0])
        soup = BeautifulSoup(res.text, 'html.parser')
        Total=''
        for index, data in enumerate(soup.select('div.tags a')):
            Total+=(self.Prefix + data['href'])+'\n'
        return Total

# ----------------------------------------------------------------------------------------------
    #取得相冊
    def Get_Album(self):
        rs = requests.session()
        res = rs.get(self.Target_url[1])
        soup = BeautifulSoup(res.text, 'html.parser')

        Title_List = []
        Link_List = []
        Total=''
        for index, data in enumerate(soup.select('div.nf-videos ul.photosAlbumsListing.displayPublic.noAd div.title-album')):
            Title_List.append(data.string)

        for index, data in enumerate(soup.select('div.nf-videos ul.photosAlbumsListing.displayPublic.noAd a')):
            Link_List.append(self.Prefix + data['href'])

        for index in range(len(Title_List)):
            Total += (Title_List[index]) + '\n'
            Total += (Link_List[index]) + '\n'
        return Total
# ----------------------------------------------------------------------------------------------