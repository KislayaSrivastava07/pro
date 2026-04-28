"""
Configuration file for Human Detection & Alarm System
Centralized parameter management
"""

# Camera Configuration
CAMERA_SOURCE = 0  # 0 = Webcam, or IP camera URL like "http://192.168.1.100:8080/video"
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FRAME_FPS = 30

# Detection Configuration
YOLO_MODEL = "yolov8n.pt"  # Options: yolov8n, yolov8s, yolov8m, yolov8l
CONFIDENCE_THRESHOLD = 0.5  # YOLO confidence threshold

# Distance Estimation Configuration
FOCAL_LENGTH = 1000  # Camera focal length in pixels (calibrate for your camera)
AVERAGE_HUMAN_HEIGHT_CM = 170  # Average human height for distance calculation

# Alarm Configuration
DISTANCE_THRESHOLD_CM = 200  # Trigger alarm if human closer than this (cm)
ALARM_FREQUENCY_HZ = 1000  # Beep frequency in Hz
ALARM_DURATION_MS = 500  # Beep duration in milliseconds
ALARM_COOLDOWN_SECONDS = 2  # Minimum time between alarms

# Display Configuration
SHOW_DETECTIONS = True
SHOW_DISTANCE = True
SHOW_STATISTICS = True
DRAW_THRESHOLD_LINE = True

# Logging Configuration
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR
LOG_TO_FILE = False
LOG_FILE_PATH = "detection_log.txt"

# Performance Configuration
USE_GPU = False  # Set to True if you have CUDA GPU
MAX_DETECTIONS_PER_FRAME = 10
FRAME_SKIP = 0  # Process every Nth frame (0 = every frame)

# Advanced Configuration
MIN_DETECTION_HEIGHT = 20  # Minimum bounding box height to consider
MIN_DETECTION_WIDTH = 20  # Minimum bounding box width to consider
TRACKING_MODE = False  # Track same person across frames

# Alert Configuration
ALERT_SOUND = True
ALERT_LOG = True
ALERT_SAVE_SNAPSHOT = False
ALERT_SNAPSHOT_DIR = "./alerts"
