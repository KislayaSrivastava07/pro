"""
Advanced Example: Human Detection with Snapshots & Logging
Extended features: save snapshots on alert, file logging, persistent records
"""

import cv2
import os
from datetime import datetime
from camera_source import CameraSource
from yolo_detector import YOLODetector
from distance_estimator import DistanceEstimator
from alarm_system import AlarmSystem


class AdvancedDetectionSystem:
    def __init__(self, config_dict):
        """Initialize with configuration dictionary"""
        self.config = config_dict
        
        self.camera = CameraSource(config_dict['CAMERA_SOURCE'])
        self.detector = YOLODetector(model_name=config_dict['YOLO_MODEL'])
        self.distance_estimator = DistanceEstimator(
            focal_length=config_dict['FOCAL_LENGTH']
        )
        self.alarm = AlarmSystem(
            alarm_sound_frequency=config_dict['ALARM_FREQUENCY_HZ'],
            alarm_sound_duration=config_dict['ALARM_DURATION_MS']
        )
        
        # Statistics
        self.stats = {
            'frames_processed': 0,
            'humans_detected': 0,
            'alarms_triggered': 0,
            'snapshots_saved': 0,
            'min_distance': float('inf')
        }
        
        # Create alert directory if enabled
        if config_dict.get('ALERT_SAVE_SNAPSHOT', False):
            os.makedirs(config_dict['ALERT_SNAPSHOT_DIR'], exist_ok=True)
        
        # Setup logging if enabled
        if config_dict.get('LOG_TO_FILE', False):
            self.log_file = open(config_dict['LOG_FILE_PATH'], 'a')
            self.log("System started")
        else:
            self.log_file = None
    
    def log(self, message):
        """Log message to file and/or console"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] {message}"
        print(log_msg)
        
        if self.log_file:
            self.log_file.write(log_msg + "\n")
            self.log_file.flush()
    
    def save_snapshot(self, frame, detection_info):
        """Save snapshot when alarm triggers"""
        alert_dir = self.config['ALERT_SNAPSHOT_DIR']
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        filename = os.path.join(alert_dir, f"alert_{timestamp}.jpg")
        
        # Add detection info to frame
        info_text = f"Distance: {detection_info['distance']:.1f}cm | Conf: {detection_info['confidence']:.2f}"
        cv2.putText(frame, info_text, (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        cv2.imwrite(filename, frame)
        self.stats['snapshots_saved'] += 1
        self.log(f"📸 Snapshot saved: {filename}")
    
    def process_detections(self, frame, detections):
        """Process each detection"""
        alerts = []
        
        for det in detections:
            distance = self.distance_estimator.estimate_distance(det['h'])
            det['distance_cm'] = distance
            
            # Update statistics
            if distance > 0 and distance < self.stats['min_distance']:
                self.stats['min_distance'] = distance
            
            # Check threshold
            if distance > 0 and distance < self.config['DISTANCE_THRESHOLD_CM']:
                det['alert'] = True
                alerts.append({
                    'distance': distance,
                    'confidence': det['confidence'],
                    'bbox': (det['x'], det['y'], det['w'], det['h'])
                })
            else:
                det['alert'] = False
        
        return alerts
    
    def run(self):
        """Main loop"""
        print("\n🚀 Advanced Detection System Running")
        print(f"   Threshold: {self.config['DISTANCE_THRESHOLD_CM']}cm")
        print(f"   Snapshot saving: {self.config.get('ALERT_SAVE_SNAPSHOT', False)}")
        print(f"   File logging: {self.config.get('LOG_TO_FILE', False)}\n")
        
        try:
            while True:
                ret, frame = self.camera.read_frame()
                if not ret:
                    break
                
                self.stats['frames_processed'] += 1
                
                # Detect humans
                detections = self.detector.detect_humans(frame)
                self.stats['humans_detected'] += len(detections)
                
                # Process detections
                alerts = self.process_detections(frame, detections)
                
                if alerts:
                    self.stats['alarms_triggered'] += len(alerts)
                    self.alarm.trigger_alarm()
                    
                    for alert in alerts:
                        distance = alert['distance']
                        self.log(f"🚨 ALERT: Human detected at {distance:.1f}cm")
                        
                        if self.config.get('ALERT_SAVE_SNAPSHOT', False):
                            self.save_snapshot(frame, alert)
                else:
                    self.alarm.stop_alarm()
                
                # Draw on frame
                frame = self.detector.draw_detections(
                    frame, detections,
                    color=(0, 0, 255) if alerts else (0, 255, 0)
                )
                
                # Draw stats
                self.draw_stats(frame)
                
                cv2.imshow("Advanced Detection System", frame)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
                elif key == ord('s'):
                    self.save_snapshot(frame, {'distance': 0, 'confidence': 0})
                elif key == ord('r'):
                    self.stats['min_distance'] = float('inf')
                    self.log("📊 Statistics reset")
        
        except KeyboardInterrupt:
            print("\n⚠️  Interrupted")
        
        finally:
            self.cleanup()
    
    def draw_stats(self, frame):
        """Draw statistics panel"""
        stats_list = [
            f"Frames: {self.stats['frames_processed']}",
            f"Humans: {self.stats['humans_detected']}",
            f"Alarms: {self.stats['alarms_triggered']}",
            f"Snapshots: {self.stats['snapshots_saved']}",
            f"Min Dist: {self.stats['min_distance']:.1f}cm"
        ]
        
        for i, text in enumerate(stats_list):
            cv2.putText(frame, text, (10, 30 + i * 25),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    def cleanup(self):
        """Cleanup"""
        self.log(f"\n📊 Final Statistics:")
        self.log(f"   Frames processed: {self.stats['frames_processed']}")
        self.log(f"   Total humans: {self.stats['humans_detected']}")
        self.log(f"   Alarms triggered: {self.stats['alarms_triggered']}")
        self.log(f"   Snapshots saved: {self.stats['snapshots_saved']}")
        
        self.alarm.stop_alarm()
        self.camera.release()
        cv2.destroyAllWindows()
        
        if self.log_file:
            self.log("System stopped")
            self.log_file.close()


# Example usage
if __name__ == "__main__":
    config = {
        'CAMERA_SOURCE': 0,
        'YOLO_MODEL': 'yolov8n.pt',
        'FOCAL_LENGTH': 1000,
        'DISTANCE_THRESHOLD_CM': 200,
        'ALARM_FREQUENCY_HZ': 1000,
        'ALARM_DURATION_MS': 500,
        'ALERT_SAVE_SNAPSHOT': True,  # Enable snapshot saving
        'ALERT_SNAPSHOT_DIR': './alerts',
        'LOG_TO_FILE': True,  # Enable file logging
        'LOG_FILE_PATH': 'detection_log.txt'
    }
    
    system = AdvancedDetectionSystem(config)
    system.run()
