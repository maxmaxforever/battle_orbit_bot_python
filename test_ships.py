"""
test_ships.py - Run this with ships clearly visible on screen
Shows ALL detections at threshold 0.01 so we can see what the model knows
"""
from capture.capture import WindowCapture
from vision.detector import Detector
import config, cv2, time

config.CONF_THRESH = 0.01
cap = WindowCapture('Space aces | Game')
det = Detector()

print("Make sure NPC ships are clearly visible on screen!")
print("Capturing in 3 seconds...")
time.sleep(3)

for i in range(3):
    frame = cap.grab()
    dets  = det.detect(frame)
    
    print(f"\nFrame {i}: {len(dets)} total detections")
    for d in dets:
        print(f"  {d.class_name:<15} conf={d.confidence:.4f}  area={d.area}  center={d.center}")
    
    # Save annotated frame so we can see what it found
    vis = det.draw(frame, dets)
    cv2.imwrite(f'ship_test_{i}.png', vis)
    print(f"  Saved ship_test_{i}.png")
    time.sleep(2)

print("\nDone - open ship_test_*.png to see what was detected")
