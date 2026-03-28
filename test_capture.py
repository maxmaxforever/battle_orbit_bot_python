from capture.capture import WindowCapture
import cv2, time

cap = WindowCapture('Space aces | Game')
for i in range(3):
    f = cap.grab()
    print(f.shape if f is not None else 'NONE')
    cv2.imwrite(f'live_test_{i}.png', f)
    time.sleep(1)