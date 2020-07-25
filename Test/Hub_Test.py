from Core.HubCore import HubCore


a=HubCore()
print(a.Hub_Photo_And_Gifs.Get_Album())


'''

Prefix='https://www.pornhub.com'
Target_url='https://www.pornhub.com/albums/female-straight'
rs = requests.session()
res = rs.get(Target_url)
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.select('div.nf-videos ul.photosAlbumsListing.displayPublic.noAd div.title-album'))



for index,data in enumerate(soup.select('div.nf-videos ul.photosAlbumsListing.displayPublic.noAd a')):

    print(Prefix+data['href'])
'''

