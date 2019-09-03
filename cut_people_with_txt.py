import cv2
import os

work_dir=os.getcwd()
image_txt_source=os.path.join(work_dir,'txt_and_image')
image_output_path=os.path.join(work_dir,'out_image')





for txt_filename in os.listdir(image_txt_source):
    if txt_filename.endswith('.txt'):
        f = open(image_txt_source+"\\"+txt_filename,'r')
        inside = str(f.read())
        
        xy = inside.split(' ')
        f.close()
        for i in xy:
            if '\n' in i:
                fix = i.replace('\n',' ')#找出\n的元素取代成空白
                fixed = fix.split(' ')#用空白分出值
                p = xy.index(i)#找出問題元素索引值
                xy.pop(p)#刪除\n的元素
                xy.insert(p,fixed[0])#插入剛剛刪除的元素位置
                xy.insert(p+1,fixed[1])#插入剛剛刪除的元素位置+1
        
                
        num_object = int(len(xy)/5)#抓出有多少數量


        without_Filename_Extension=txt_filename.split('.')[0]
        image = cv2.imread(image_txt_source+"\\"+without_Filename_Extension+'.jpg')
        image_size_w=image.shape[1]
        image_size_h=image.shape[0]

        for o in range(0,num_object):
                first_index = o*5
                x = float(xy[first_index+1])
                y = float(xy[first_index+2])
                w = float(xy[first_index+3])    
                h = float(xy[first_index+4])
                
                xmin = int(round(((2*x*image_size_w)-(w*image_size_w))/2,0))
                xmax = int(round(((2*x*image_size_w)+(w*image_size_w))/2,0))
                ymin = int(round(((2*y*image_size_h)-(h*image_size_h))/2,0))
                ymax = int(round(((2*y*image_size_h)+(h*image_size_h))/2,0))

                crog_img = image[ymin:ymax,xmin:xmax]
                if cv2.imwrite(image_output_path+"\\"+without_Filename_Extension+'_'+str(o)+'.jpg',crog_img):
                        print(f'{txt_filename}擷取成功')
                else:
                        log = open('log.txt','a')
                        log.write(f'{txt_filename}''\n')
                        print(f'{txt_filename}擷取失敗')

        