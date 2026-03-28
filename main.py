"""
main.py
=======
Entry point for the Battle Orbit bot.

Usage
-----
    # 1. Just run the bot (requires trained weights in vision/weights/best.pt)
    python main.py

    # 2. Collect training data only
    python main.py --collect

    # 3. Auto-label collected images
    python main.py --autolabel

    # 4. Train the YOLO model
    python main.py --train

    # 5. Debug — show live detections without running the bot
    python main.py --debug
"""

import argparse
import sys
import time

import win32gui

import config
from utils.logger import get_logger

log = get_logger("main")


def get_window_offset():
    """Return (x, y) top-left of the game window in screen coords."""
    hwnd = win32gui.FindWindow(None, config.WINDOW_TITLE)
    if not hwnd:
        log.warning(f"Window '{config.WINDOW_TITLE}' not found — offset defaulting to (0, 0)")
        return 0, 0
    left, top, _, _ = win32gui.GetWindowRect(hwnd)
    return left, top


def run_bot():
    from bot.fsm import BotFSM
    offset = get_window_offset()
    log.info(f"Window offset: {offset}")
    log.info("Starting bot in 3 seconds — switch to game window …")
    time.sleep(3)
    BotFSM(window_offset=offset).run()


def run_collect():
    from data.collect import DataCollector
    DataCollector().run()


def run_autolabel():
    from data.autolabel import autolabel_all
    autolabel_all()


def run_train():
    from train.train import train
    train()


def run_debug():
    """Show live YOLO detections overlaid on the captured window."""
    import cv2
    from capture.capture import WindowCapture
    from vision.detector import Detector

    cap = WindowCapture(config.WINDOW_TITLE)
    det = Detector()

    log.info("Debug mode — press ESC to quit.")
    while True:
        frame = cap.grab()
        if frame is None:
            time.sleep(0.1)
            continue

        dets = det.detect(frame)
        vis  = det.draw(frame, dets)

        # Overlay FPS and state info
        import cv2 as _cv2
        _cv2.putText(vis, f"Detections: {len(dets)}", (10, 30),
                     _cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        _cv2.imshow("Battle Orbit — Debug", vis)

        if _cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()


# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Battle Orbit Bot")
    parser.add_argument("--collect",   action="store_true", help="Run data collector")
    parser.add_argument("--autolabel", action="store_true", help="Auto-label images")
    parser.add_argument("--train",     action="store_true", help="Train YOLOv8 model")
    parser.add_argument("--debug",     action="store_true", help="Debug detection overlay")
    args = parser.parse_args()

    if args.collect:
        run_collect()
    elif args.autolabel:
        run_autolabel()
    elif args.train:
        run_train()
    elif args.debug:
        run_debug()
    else:
        run_bot()


if __name__ == "__main__":
    main()
