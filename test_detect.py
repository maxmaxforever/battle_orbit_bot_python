from capture.capture import WindowCapture
from vision.detector import Detector
import config, time

config.CONF_THRESH = 0.01  # basically zero - show everything
cap = WindowCapture('Space aces | Game')
det = Detector()

for i in range(5):
    frame = cap.grab()
    dets  = det.detect(frame)
    print(f"Frame {i}: {len(dets)} detections")
    for d in dets:
        print(f"  {d.class_name} conf={d.confidence:.3f} area={d.area}")
    time.sleep(1)