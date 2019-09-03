import cv2
import os

work_dir=os.getcwd()
image_txt_source=os.path.join(work_dir,'txt_and_image')
image_output_path=os.path.join(work_dir,'out_image')
notxt_img=[]

for img_filename in os.listdir(image_txt_source):
    if img_filename.endswith('.jpg'):
        iname = img_filename.split('.')
        join_txt = str(iname[0])+'.txt'
        try:
            f = open(image_txt_source+'\\'+join_txt,'r')
            content = f.read()
            f.close()
        except FileNotFoundError:
            notxt_img.append(img_filename)
            print(f'{img_filename}'"檔案不存在txt。")
        # 路徑為目錄的例外處理
        except IsADirectoryError:
            print("該路徑為目錄")
'''
for i in notxt_img:
    try:
        os.remove(image_txt_source+'\\'+str(i))
    except OSError as e:
        print(e)
    else:
        print("File is deleted successfully")
