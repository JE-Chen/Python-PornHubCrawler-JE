from HubVideo import HubVideo
from HubStar import HubStar
from HubCategories import HubCategories
from Hub_Photo_And_Gifs import Hub_Photo_And_Gifs

class HubCore():

    def __init__(self):
        self.HubStar=HubStar()
        self.HubVideo=HubVideo()
        self.HubCategories=HubCategories()
        self.Hub_Photo_And_Gifs=Hub_Photo_And_Gifs()