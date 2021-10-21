import numpy as np
import cv2
from PIL import ImageGrab
import time

count=0
while 1:
    count=count+1
    img = ImageGrab.grab(bbox=(0,0,1920,1080))#xmin xmax ymin ymax
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('s',frame)

    if(count==30):
        print(count)
        t = time.time()*1000
        cv2.imwrite('./datafootball/'+str(int(t))+'.png',frame)
        count = 0

    cv2.waitKey(5)
    cv2.destroyAllWindows()