import os

images = os.listdir('labels_basketball')

i = 1
for image in images:
    if image.startswith('train'):
        prefix = '0000'
        if i < 10:
            prefix = prefix+'0'
        os.rename('labels_basketball/'+str(image), 'labels_basketball/'+prefix+str(i)+'.xml')
    i += 1
