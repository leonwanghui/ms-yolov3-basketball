# import os

# images = os.listdir('labels')

# i = 1
# for image in images:
#     if image.startswith('train'):
#         prefix = '0000'
#         if i < 10:
#             prefix = prefix+'0'
#         os.rename('labels/'+str(image), 'labels/'+prefix+str(i)+'.xml')
#         i += 1

################################################################
# import os

# labels = os.listdir('labels')

# if os.path.exists("xmllist.txt"):
#     os.remove("xmllist.txt")

# file_obj = open('xmllist.txt', 'w')
# for label in labels:
#     file_obj.writelines(label)
#     file_obj.write('\n')
# file_obj.close()
