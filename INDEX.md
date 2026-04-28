# 📚 DOCUMENTATION INDEX

Welcome to the Human Detection & Alarm System! Use this index to find what you need.

## 🚀 START HERE

### First Time Setup?
→ Read: **SETUP.md**
- Installation instructions
- Camera configuration
- Troubleshooting guide

### Need Quick Answers?
→ Read: **QUICK_REF.md**
- Common configuration changes
- Keyboard controls
- Troubleshooting table

### Want to Understand the System?
→ Read: **README.md**
- Feature overview
- Component descriptions
- Performance tips

## 📁 FILE GUIDE

### 🎯 Core Application Files

#### **main.py** (START HERE)
- Main application entry point
- 152 lines of well-commented code
- Configurable parameters at top
- Run with: `python main.py`

#### **camera_source.py**
- Handles webcam/IP camera frame capture
- Sets resolution, FPS, camera properties
- Used by main.py automatically

#### **yolo_detector.py**
- YOLOv8 neural network for human detection
- Draws bounding boxes and confidence scores
- Used by main.py automatically

#### **distance_estimator.py**
- Calculates distance using focal length method
- Interactive calibration support
- Used by main.py automatically

#### **alarm_system.py**
- Triggers alarm when threshold exceeded
- Non-blocking threaded alarm
- Event logging with timestamps

### 🛠️ Tools & Utilities

#### **test_setup.py** (RUN THIS FIRST)
- Verifies all packages installed
- Tests webcam access
- Tests YOLO model loading
- Tests individual components
- Run with: `python test_setup.py`

#### **advanced_example.py**
- Extended features beyond basic system
- Snapshot saving on alert
- Event logging to file
- Persistent statistics
- Run with: `python advanced_example.py`

#### **config.py**
- All configuration parameters in one place
- Centralized settings management
- Easily switch between profiles

### 📖 Documentation Files

#### **README.md** (Feature Overview)
Best for understanding:
- What the system does
- How each component works
- Performance tips
- Integration ideas

#### **SETUP.md** (Installation Guide)
Best for:
- Initial installation
- Camera configuration
- Step-by-step verification
- Detailed troubleshooting

#### **QUICK_REF.md** (Quick Reference)
Best for:
- Quick configuration changes
- Keyboard controls
- Fast troubleshooting
- Common modifications

#### **PROJECT_SUMMARY.md** (This Project)
Best for:
- Project overview
- Files list and purposes
- Architecture diagram
- Technology stack

#### **requirements.txt** (Dependencies)
Lists all Python packages needed:
- opencv-python
- numpy
- ultralytics

## 🎮 WORKFLOW GUIDE

### Scenario 1: I Just Downloaded This

```
1. Read: SETUP.md (Installation section)
2. Run:  pip install -r requirements.txt
3. Run:  python test_setup.py
4. Read: QUICK_REF.md (Getting Started)
5. Run:  python main.py
```

### Scenario 2: I Need to Change Settings

```
1. Check: QUICK_REF.md (Configuration section)
2. Edit:  main.py (find parameter to change)
3. Rerun: python main.py
```

### Scenario 3: Something Doesn't Work

```
1. Check: QUICK_REF.md (Troubleshooting table)
2. Read:  SETUP.md (Troubleshooting section)
3. Run:   python test_setup.py (find which part fails)
4. Fix:   Follow solution in SETUP.md
```

### Scenario 4: I Want Advanced Features

```
1. Read:  README.md (Features section)
2. Edit:  advanced_example.py or config.py
3. Run:   python advanced_example.py
```

### Scenario 5: I Want to Understand the Code

```
1. Start:    main.py (read top section with comments)
2. Explore:  camera_source.py (understand frame capture)
3. Explore:  yolo_detector.py (understand detection)
4. Explore:  distance_estimator.py (understand distance calc)
5. Explore:  alarm_system.py (understand alarm)
```

## 📊 DECISION TREE

```
What do you want to do?
│
├─ Setup the system
│   └─ Read: SETUP.md
│
├─ Run the system
│   ├─ First time?
│   │   └─ Run: python test_setup.py (verify setup first)
│   │
│   └─ Ready to run?
│       └─ Run: python main.py
│
├─ Change settings
│   ├─ Want quick reference?
│   │   └─ Read: QUICK_REF.md
│   │
│   └─ Want detailed explanation?
│       └─ Read: README.md
│
├─ Fix a problem
│   ├─ Is it installation?
│   │   └─ Read: SETUP.md → Troubleshooting
│   │
│   └─ Is it runtime?
│       ├─ Check: QUICK_REF.md → Troubleshooting table
│       │
│       └─ Run: python test_setup.py
│
├─ Understand the code
│   ├─ Quick overview?
│   │   └─ Read: PROJECT_SUMMARY.md → Architecture
│   │
│   ├─ Feature details?
│   │   └─ Read: README.md
│   │
│   └─ Deep dive?
│       └─ Read: Code files with inline comments
│
└─ Extend the system
    ├─ Add features?
    │   └─ See: advanced_example.py
    │
    └─ Ideas for extensions?
        └─ Read: README.md → Integration Ideas section
```

## 🔍 QUICK SEARCH

### By Task
| Task | Read This | File |
|------|-----------|------|
| Install system | SETUP.md | - |
| Run system | QUICK_REF.md | main.py |
| Configure settings | QUICK_REF.md | config.py or main.py |
| Calibrate camera | SETUP.md | main.py (press 'c') |
| Fix problems | SETUP.md (Troubleshooting) | - |
| Understand architecture | PROJECT_SUMMARY.md | - |
| Learn component details | README.md | Component files |
| Add advanced features | advanced_example.py | - |

### By File
| File | Purpose | Read When |
|------|---------|-----------|
| main.py | Main app | Want to run or modify |
| camera_source.py | Camera handling | Want to change camera |
| yolo_detector.py | Detection | Want to change model |
| distance_estimator.py | Distance calc | Want to calibrate |
| alarm_system.py | Alarm logic | Want to customize alarm |
| test_setup.py | Verification | Problem setup |
| advanced_example.py | Advanced features | Want snapshots/logging |
| config.py | All settings | Want reference |
| README.md | Feature overview | Want to understand features |
| SETUP.md | Installation | First time setup |
| QUICK_REF.md | Quick help | Quick answers |
| PROJECT_SUMMARY.md | Project overview | Want big picture |

## ⚡ MOST COMMON QUESTIONS

### Q: How do I run this?
**A:** `python test_setup.py` then `python main.py`  
**See:** QUICK_REF.md → Fastest Setup

### Q: Where do I change the alarm distance?
**A:** Edit main.py, change `DISTANCE_THRESHOLD_CM`  
**See:** QUICK_REF.md → Common Configuration Changes

### Q: How do I use IP camera?
**A:** Edit main.py, change `CAMERA_SOURCE` to camera URL  
**See:** QUICK_REF.md → Common Configuration Changes

### Q: What if I get an error?
**A:** Run `python test_setup.py` to find the problem  
**See:** SETUP.md → Troubleshooting section

### Q: How do I calibrate the distance?
**A:** Run system, press 'c' during execution  
**See:** SETUP.md → Step 5: Calibrate Distance

### Q: Which files do I edit?
**A:** Only main.py (for basic setup) or config.py (for reference)  
**See:** QUICK_REF.md → Files by Purpose

## 📚 RECOMMENDED READING ORDER

### For Users (Just Want to Run It)
1. SETUP.md (Installation section)
2. QUICK_REF.md (Getting Started)
3. Run the system
4. Reference as needed

### For Developers (Want to Understand Code)
1. PROJECT_SUMMARY.md (Overview)
2. README.md (Features & Components)
3. Source code (main.py, then component files)
4. advanced_example.py (Extended patterns)

### For Customizers (Want to Modify Behavior)
1. QUICK_REF.md (Common Changes)
2. config.py (See all parameters)
3. main.py (Edit as needed)
4. SETUP.md (Troubleshoot if issues)

## 🎯 NAVIGATION LINKS

- 🚀 **Quick Start**: QUICK_REF.md → Fastest Setup
- 📥 **Installation**: SETUP.md → Step 1-7
- ⚙️ **Configuration**: QUICK_REF.md → Common Configuration Changes
- 🆘 **Help**: SETUP.md → Troubleshooting section
- 🏗️ **Architecture**: PROJECT_SUMMARY.md → Architecture Overview
- 💻 **Code**: main.py → lines 1-50 (comments)
- 🔧 **Tools**: test_setup.py (verification)

## ✅ VERIFICATION CHECKLIST

After reading documentation:
- [ ] Packages installed: `pip list` check
- [ ] Setup verified: `python test_setup.py` passes
- [ ] System runs: `python main.py` shows video
- [ ] Humans detected: Bounding boxes appear
- [ ] Distance shown: Numbers display in cm
- [ ] Alarm works: Triggers when person gets close

---

**Still stuck?**
1. Run: `python test_setup.py` (shows what's working)
2. Check: SETUP.md → Troubleshooting (matches your error)
3. Ask: Check console output for error details

**Everything working?**
→ Congratulations! 🎉 Now explore QUICK_REF.md for customization options.

