#-*-coding="utf-8"-*-
import os
import sys
import cv2

work_path=os.getcwd()
image_path=os.path.join(work_path,'out_image')
ooutput_path=os.path.join(work_path,'150X240')

need_to_resize_list=[]
for imgName in os.listdir(image_path):
    if imgName.endswith('.jpg') or imgName.endswith('.jepg'):
        need_to_resize_list.append(imgName)

for img in  need_to_resize_list:
    image=cv2.imread(image_path+'\\'+img)
    if image.shape[0] != 150 or image.shape[1] != 240:
        reimg = cv2.resize(image,(150,240),interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(ooutput_path+'\\'+img,reimg)
        print(f'{img}轉換成功到150X240')
    else:
        print(f'{img} 沒有轉換，大小剛剛好')
        cv2.imwrite(ooutput_path+'\\'+img,image)
        print(f'{img} 轉過去了150X240資料夾')