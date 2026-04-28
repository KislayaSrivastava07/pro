# 🎥 Human Detection & Alarm System

A complete computer vision system that detects humans using YOLO, estimates distance, and triggers an alarm if they get too close.

## 📋 System Pipeline

```
IP Camera / Webcam
        ↓
Frame Capture (camera_source.py)
        ↓
Human Detection - YOLO (yolo_detector.py)
        ↓
Estimate Distance (distance_estimator.py)
        ↓
Compare with Threshold
        ↓
Trigger Alarm (alarm_system.py)
```

## 🎯 Features

- ✅ Real-time human detection using YOLOv8 Nano
- ✅ Distance estimation using focal length method
- ✅ Automatic alarm triggering when threshold exceeded
- ✅ Support for webcam and IP cameras
- ✅ Live statistics and visualization
- ✅ Distance calibration mode
- ✅ Interactive controls during runtime

## 📦 Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. What Gets Installed

- **opencv-python**: Computer vision library
- **numpy**: Numerical computing
- **ultralytics**: YOLO framework (will auto-download yolov8n.pt model on first run)

## 🚀 Quick Start

### Run with Webcam

```bash
python main.py
```

### Run with IP Camera

Edit `main.py` line with CAMERA_SOURCE:
```python
CAMERA_SOURCE = "http://192.168.1.100:8080/video"  # Replace with your camera URL
```

## 🎮 Keyboard Controls During Runtime

| Key | Action |
|-----|--------|
| `q` | Quit application |
| `r` | Reset statistics |
| `c` | Calibrate distance (interactive) |

## ⚙️ Configuration

Edit these values in `main.py`:

```python
CAMERA_SOURCE = 0                    # 0 = webcam, or IP camera URL
DISTANCE_THRESHOLD_CM = 200          # Alarm triggers if human closer than 200cm
FOCAL_LENGTH = 1000                  # Camera focal length (calibrate for accuracy)
```

## 📏 Calibration Guide

For accurate distance estimation, calibrate your camera:

1. Run the application
2. Press `c` to enter calibration mode
3. Stand at a known distance (e.g., 1 meter = 100cm) from camera
4. Press SPACE when detected
5. Enter the distance in cm
6. System will calculate and save focal length

**Note:** Focal length depends on your camera. Better calibration = better accuracy.

## 📁 Project Structure

```
project/
├── main.py                    # Main application (run this)
├── camera_source.py           # Webcam/IP camera frame capture
├── yolo_detector.py           # YOLOv8 human detection
├── distance_estimator.py      # Distance calculation
├── alarm_system.py            # Alarm triggering logic
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🔧 Component Details

### camera_source.py
- Handles frame capture from webcam or IP camera
- Manages video stream properties (resolution, FPS)
- Thread-safe frame reading

### yolo_detector.py
- YOLOv8 Nano model for fast detection
- Filters only "person" class (class_id = 0)
- Configurable confidence threshold
- Draws bounding boxes with confidence scores

### distance_estimator.py
- Uses focal length method: `Distance = (height * focal_length) / bbox_height`
- Configurable average human height (default: 170cm)
- Interactive calibration support

### alarm_system.py
- Windows beep alarm (cross-platform support)
- Non-blocking alarm thread
- Event logging with timestamps
- Configurable frequency and duration

## 📊 Output Display

The live display shows:
- Bounding boxes around detected humans (green)
- Distance to each person in cm
- Threshold line for reference
- Real-time statistics panel:
  - Frame count
  - Total humans detected
  - Minimum distance recorded
  - Alarm status

## 🎨 Troubleshooting

### No detections?
- Ensure good lighting
- Adjust confidence threshold in `yolo_detector.py`
- Ensure whole human body is visible

### Alarm won't work?
- Increase distance threshold value
- Calibrate your camera for accurate distances

### Slow FPS?
- Use smaller model: `yolov8n.pt` (already set)
- Reduce frame resolution in `camera_source.py`
- Use GPU acceleration (CUDA)

### IP Camera Connection?
- Verify camera URL and network connection
- Try accessing URL in browser first
- Check camera credentials/firewall

## 🚨 Alarm Configuration

Customize alarm in `alarm_system.py`:

```python
# Change beep frequency and duration
AlarmSystem(alarm_sound_frequency=1500, alarm_sound_duration=300)
```

## 📝 Example Usage Scenarios

1. **Security System**: Trigger alarm if person enters restricted zone
2. **Occupancy Detection**: Count humans in room
3. **Social Distancing**: Alert when people too close
4. **Parking Lot**: Detect unauthorized persons
5. **Workplace Safety**: Monitor restricted areas

## 🔄 Performance Tips

- Use `yolov8n.pt` for real-time (default)
- Use `yolov8s.pt` for better accuracy (slower)
- Calibrate focal length for your specific camera
- Adjust frame resolution based on camera capabilities
- Use GPU if available (install `torch[cuda]`)

## 📚 Dependencies Explained

| Package | Purpose | Version |
|---------|---------|---------|
| opencv-python | Video/image processing | 4.8.1.78 |
| numpy | Numerical operations | 1.24.3 |
| ultralytics | YOLO framework | 8.0.147 |

## 🤝 Integration Ideas

- Connect to security system via API
- Send email/SMS alerts on detection
- Save snapshot images on trigger
- Store detection logs to database
- Multi-camera support

## 📄 License

Free to use and modify

## 💡 Notes

- First run will download YOLOv8 model (~25MB)
- Works on Windows, Mac, Linux
- GPU acceleration available with CUDA
- Model is cached after first download

---

**Questions?** Debug output shows detailed information at each step. Check the console for error messages.
