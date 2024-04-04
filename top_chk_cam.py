import os
# opencvをインポートする前にこの処理を加えると起動が早くなる
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2, sys

cam_num = sys.argv[1]

# 最後に記録されたマウスの位置
last_mouse_position = (0, 0)

# マウスイベントのコールバック関数
def mouse_event(event, x, y, flags, param):
    global last_mouse_position
    if event == cv2.EVENT_MOUSEMOVE:
        last_mouse_position = (x, y)

# カメラキャプチャの開始
cap = cv2.VideoCapture(int(cam_num))

# カメラ解像度の設定
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 4096)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', mouse_event)

while(True):
    # フレームをキャプチャ
    ret, frame = cap.read()

    # フレームが正しくキャプチャできた場合のみ処理を行う
    if ret:
        # マウスの位置にテキストを描画
        x, y = last_mouse_position
        cv2.putText(frame, f"X: {x}, Y: {y}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        print(f"X: {x}, Y: {y}")
        
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break

# すべてのウィンドウを閉じる
cap.release()
cv2.destroyAllWindows()
