import requests as r, random, os
from multiprocessing import Process



if os.path.exists('wallhaven'):
    print('Folder alredy exists')
else:
    os.makedirs('wallhaven')
    print('Working folder successfuly created')
os.chdir('wallhaven')
allpic = int(input('Enter current amount of pictures: '))
def start():
    downloads = 1
    for donwloads in range(allpic, 0, -1):
        picid = random.randint(1,allpic)
        ext = 'jpg'
        picname = 'wallhaven-{}.{}'.format(picid,ext)
        if os.path.exists(picname):
            print('Image with ID:{} alredy exists'.format(picid))
        else:
            pic = r.get('http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}.{}'.format(picid,ext))
            if pic.status_code == 404:
                print('Picture with id {}. Not found... Trying to change to png...'.format(picid))
                ext = 'png'
                pic = r.get('http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}.{}'.format(picid,ext))
            if pic.status_code != 404:
                out = open('wallhaven-{}.{}'.format(picid,ext), 'wb')
                out.write(pic.content)
                out.close()
        if pic.status_code == 404:
            print('Image with id:{} NOT FOUND(404 response). Deleting file...'.format(picid))
        else:
            print('Image {}/{} downloaded. ID:{}'.format(downloads,allpic,picid))
        downloads = downloads + 1
        
if __name__ == '__main__':
    i = 0
    while i < 4:
        i = Process(target = start(), args= ())
        i.start()
        i = i + 1
print('Done!')
