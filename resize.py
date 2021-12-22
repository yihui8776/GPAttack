import os
from PIL import  Image

def refile(file_dir):
    for root,dirs,files in  os.walk(file_dir):
        count= 1
        for i in files:
            if i.endswith('.jpg'):
                im = Image.open(file_dir+'/'+i)
                out = im.resize((500,500))
                #out.save('./image/'+i.split('.')[0]+'.png','PNG')
                out.save('./images/'+str(count)+'.png','PNG')
                count+=1
                print(count)


if __name__ == "__main__":
    refile('./image')
