import requests as r, random, os

allpic=''
downloads=0

if os.path.exists('wallhaven'):
    print('Folder alredy exists')
else:
    os.makedirs('wallhaven')
    print('Working folder successfuly created')
os.chdir('wallhaven')
allpic=input('Enter current amount of pictures: ')
allpic = int(str(allpic))
while downloads < allpic:
    ext='jpg'
    picid=random.randint(1,allpic)
    pic=r.get('http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}.{}'.format(picid,ext))
    if pic == '<Response [404]>':
        ext='png'
        pic=r.get('http://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-{}.{}'.format(picid,ext))
    picname='wallhaven-{}.{}'.format(picid,ext)
    if os.path.exists(picname):
        print('Image with ID:{} alredy exists'.format(picid))
    else:
        out=open('{}'.format(picname), 'wb')
        out.write(pic.content)
        out.close()
    if os.path.getsize(picname) == 162:
        print('Image with id:{} NOT FOUND(404 response). Deleting file...'.format(picid))
        os.remove(picname)
    else:
        print('Image {}/{} downloaded. ID:{}'.format(downloads,allpic,picid))
    downloads = downloads + 1
print('Done!')
