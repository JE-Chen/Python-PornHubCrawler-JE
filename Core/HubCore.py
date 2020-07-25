import datetime
import sys
from Models.HubVideo import HubVideo
from Models.HubStar import HubStar
from Models.HubCategories import HubCategories
from Models.Hub_Photo_And_Gifs import Hub_Photo_And_Gifs

class HubCore():

    def __init__(self):
        try:
            self.HubStar=HubStar()
            self.HubVideo=HubVideo()
            self.HubCategories=HubCategories()
            self.Hub_Photo_And_Gifs=Hub_Photo_And_Gifs()
        except Exception as Errr:
            print(Errr)
            sys.exit()
        print(datetime.datetime.now(),self.__class__,'Ready',sep=' ')
