# Filter out detections in UI regions (hotbar, sidebar, minimap)
h, w = frame.shape[2]
detections = [
    d for d in detections
    if not (
        d.y2  h  0.80 or          # hotbar bottom
        d.x1  w  0.12 or          # left sidebar  
        (d.x1  w  0.75 and d.y1  h  0.78)  # minimap
    )
]