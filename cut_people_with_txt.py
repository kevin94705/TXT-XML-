import cv2
import os

work_dir=os.getcwd()
image_txt_source=os.path.join(work_dir,'txt_and_image')
image_output_path=os.path.join(work_dir,'out_image')

image_size_w=1280
image_size_h=720

for txt_filename in os.listdir(image_txt_source):
    if txt_filename.endswith('.txt'):
        f = open(image_txt_source+"\\"+txt_filename,'r')
        inside = str(f.read())
        print(txt_filename)
        xy = inside.split(' ')
        x = float(xy[1])
        y = float(xy[2])
        w = float(xy[3])    
        h = float(xy[4])
        xmin = int(round(((2*x*image_size_w)-(w*image_size_w))/2,0))
        xmax = int(round(((2*x*image_size_w)+(w*image_size_w))/2,0))
        ymin = int(round(((2*y*image_size_h)-(h*image_size_h))/2,0))
        ymax = int(round(((2*y*image_size_h)+(h*image_size_h))/2,0))
        
        without_Filename_Extension=txt_filename.split('.')[0]        
        f.close()
        img = cv2.imread(image_txt_source+"\\"+without_Filename_Extension+'.jpg')
        crog_img = img[ymin:ymax,xmin:xmax]
        cv2.imwrite(image_output_path+"\\"+without_Filename_Extension+'.jpg',crog_img)
        