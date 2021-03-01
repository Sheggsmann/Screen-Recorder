import numpy as np
import cv2
from PIL import ImageGrab



# Declare the fourcc variable
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
vid = cv2.VideoWriter('output2.mp4', fourcc, 5.0, (640, 480))



while True:
    img = ImageGrab.grab()

    arr = np.array(img)

    frame = cv2.cvtColor(arr, cv2.COLOR_BGR2RGB)

    cv2.imshow("Recorder", frame)
    vid.write(frame)

    if cv2.waitKey(1) == ord('q'):
        break


vid.release()
cv2.destroyAllWindows()


# In this tutorial, I am going to show you guys how to decieve your self in python.