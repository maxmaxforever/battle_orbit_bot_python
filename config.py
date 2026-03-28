# ============================================================
#  Battle Orbit Bot — Central Configuration
# ============================================================

# --- Window ---
WINDOW_TITLE = "Space aces | Game"          # Electron window title (adjust if needed)
CAPTURE_FPS   = 60                     # Target capture / inference FPS

# --- Vision ---
MODEL_PATH    = "vision/weights/best.pt"   # Trained YOLOv8 weights
CONF_THRESH   = 0.01                        # Detection confidence threshold
IOU_THRESH    = 0.40                        # NMS IoU threshold
IMG_SIZE      = 640                         # YOLO input size

# --- Class labels (must match your training labels) ---
CLASSES = {
    0: "enemy_ship",
    1: "npc_ship",
    2: "bonus_box",
    3: "own_ship",
    4: "health_bar",
}

# --- Bot timing (seconds) ---
LOOT_TRAVEL_TIME = 3.0   # seconds to wait for ship to reach a box - tune per ship
REACTION_MIN  = 0.18    # Min delay before acting (human-like lower bound)
REACTION_MAX  = 0.45    # Max delay before acting
SHOOT_KEY     = "ctrl"  # Key used to shoot (ctrl or ammo key string)
LOOT_WINDOW   = 0.55    # Seconds the bonus box stays collectable
MOVE_HOLD_MS  = 80      # How long to hold click when moving on the space map

# --- Input humanisation ---
MOUSE_SPEED_MIN = 0.10  # Seconds for fastest mouse movement
MOUSE_SPEED_MAX = 0.30  # Seconds for slowest mouse movement
JITTER_PX       = 1     # Max random pixel jitter on clicks

# --- Data collection ---
DATA_DIR      = "data/images"
LABEL_DIR     = "data/labels"
CAPTURE_KEY   = "f8"    # Hotkey to snapshot a frame during data collection

# --- Training ---
EPOCHS        = 100
BATCH_SIZE    = 16
TRAIN_IMGSZ   = 640
DEVICE        = "0"     # GPU index ("0" = first GPU, "cpu" for no GPU)
