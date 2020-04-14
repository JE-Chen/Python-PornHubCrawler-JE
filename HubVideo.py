from bs4 import BeautifulSoup
import requests

class HubVideo():


    def __init__(self):
        self.Prefix='https://www.pornhub.com'
        self.Target_url = [
            'https://cn.pornhub.com/', #Main
            'https://www.pornhub.com/video?o=ht', #GlobalHot
            'https://www.pornhub.com/video?o=mv', #MostViewed
            'https://www.pornhub.com/video?o=tr', #TopRated
            'https://www.pornhub.com/video?p=homemade&o=tr', #Homemade
            'https://www.pornhub.com/playlists',#Playlist
            'https://www.pornhub.com/channels' #Channel
        ]

# ----------------------------------------------------------------------------------------------
    #取得主頁影片
    def Get_Main_Video(self):
        rs = requests.session()
        res = rs.get(self.Target_url[0])
        soup = BeautifulSoup(res.text, 'html.parser')
        Main = soup.select('ul.videos-morepad a.linkVideoThumb')
        Total=''
        print('------------------------國際熱門------------------------------------')
        for index, data in enumerate(Main):
            print(data['title'])
            Total+=data['title']+'\n'
            print(self.Prefix + data['href'])
            Total += self.Prefix + data['href']+'\n'
        print('------------------------國際熱門------------------------------------')
        return Total

# ----------------------------------------------------------------------------------------------

    #取得熱門撥放清單
    def Get_Hot_Playlist(self):
        Play_List_Title = []
        Play_List_Href = []
        rs = requests.session()
        res = rs.get( self.Target_url[5])
        soup = BeautifulSoup(res.text, 'html.parser')
        Total=''
        for index, data in enumerate(soup.select('ul.videos.user-playlist.playlist-listing li.full-width a.title')):
            Play_List_Title.append(data['title'])

        for index, data in enumerate(
                soup.select('ul.videos.user-playlist.playlist-listing li.full-width a.playAllLink')):
            Play_List_Href.append(data['href'])

        for index in range(len(Play_List_Href)):
            Total+=(Play_List_Title[index])+'\n'
            Total+=(self.Prefix+Play_List_Href[index])+'\n'
        return Total

# ----------------------------------------------------------------------------------------------
    #取得頻道
    def Get_Channel(self):
        rs = requests.session()
        res = rs.get('https://www.pornhub.com/channels')
        soup = BeautifulSoup(res.text, 'html.parser')
        Total=''
        for index, data in enumerate(soup.select('div.container .clearfix.listChannelsWrapper ul.channelGridWrapper a.usernameLink')):
            Total+=(data.string)+'\n'
            Total+=('https://www.pornhub.com' + data['href'])+'\n'
        return Total

# ----------------------------------------------------------------------------------------------
    #取得通用影片用
    def Get_Video(self,List_Index):
        rs = requests.session()
        res = rs.get(self.Target_url[List_Index])
        soup = BeautifulSoup(res.text, 'html.parser')
        Search = soup.select('ul#videoCategory a.linkVideoThumb')
        Total = ''
        for index, data in enumerate(Search):
            print(data['title'])
            Total += data['title'] + '\n'
            print(self.Prefix + data['href'])
            Total += self.Prefix + data['href'] + '\n'
        return Total

# ----------------------------------------------------------------------------------------------

    '''
    全球熱門
    '''
    def Get_GlobalHot(self):
        return self.Get_Video(1)

# ----------------------------------------------------------------------------------------------

    '''
    全球最多觀看
    '''
    def Get_MostViewed(self):
        return self.Get_Video(2)

# ----------------------------------------------------------------------------------------------

    '''
    全球評分最高
    '''
    def Get_TopRated(self):
        return self.Get_Video(3)

# ----------------------------------------------------------------------------------------------

    '''
    全球本周最佳自製
    '''
    def Get_Homemake(self):
        return self.Get_Video(4)

# ----------------------------------------------------------------------------------------------
