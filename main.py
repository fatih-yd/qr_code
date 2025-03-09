import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    frame = cv2.flip(frame, 1)

    if not ret:
        print("görüntü alınamadı")
        break

    qr_codes = decode(frame)
    print(qr_codes)
    for qr in qr_codes:
        qr_text = qr.data.decode("utf-8")
        print(qr_text)
        pts = qr.polygon
        #print(pts)

        pts_list = []
        for i in pts:
            pts_list.append((i.x,i.y))
        print(pts_list)
        cv2.polylines(frame,[np.array(pts_list, np.int32)],True,(255,0,255),3)
        cv2.putText(frame, qr_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)










    cv2.imshow("cam",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()







