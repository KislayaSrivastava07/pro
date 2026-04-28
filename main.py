"""
Human Detection & Alarm System
Main application that combines all components
"""

import cv2
import sys
from camera_source import CameraSource
from yolo_detector import YOLODetector
from distance_estimator import DistanceEstimator
from alarm_system import AlarmSystem


class HumanDetectionAlarmSystem:
    def __init__(self, camera_source=0, distance_threshold_cm=200, focal_length=1000):
        """
        Initialize the system
        
        Args:
            camera_source: 0 for webcam or IP camera URL
            distance_threshold_cm: Trigger alarm if human is closer than this (cm)
            focal_length: Camera focal length for distance estimation
        """
        print("🚀 Initializing Human Detection & Alarm System...")
        
        self.camera = CameraSource(camera_source)
        self.detector = YOLODetector(model_name='yolov8n.pt')
        self.distance_estimator = DistanceEstimator(focal_length=focal_length)
        self.alarm = AlarmSystem()
        
        self.distance_threshold_cm = distance_threshold_cm
        self.min_distance_detected = float('inf')
        self.humans_detected_count = 0
        self.frames_processed = 0
        self.alarm_active = False
        
        width, height = self.camera.get_frame_size()
        print(f"✓ Camera initialized: {width}x{height}")
        print(f"✓ Distance threshold: {distance_threshold_cm}cm")
        print(f"✓ Model: YOLOv8 Nano")
        print("\nSystem ready! Press 'q' to quit, 'r' to reset, 'c' to calibrate\n")
    
    def process_frame(self, frame):
        """Process single frame through the pipeline"""
        # Step 1: Detect humans using YOLO
        detections = self.detector.detect_humans(frame)
        
        if detections:
            self.humans_detected_count += len(detections)
            
            # Step 2: Estimate distance for each detection
            for i, det in enumerate(detections):
                distance_cm = self.distance_estimator.estimate_distance(det['h'])
                det['distance_cm'] = distance_cm
                
                # Track minimum distance
                if distance_cm > 0 and distance_cm < self.min_distance_detected:
                    self.min_distance_detected = distance_cm
                
                # Step 3 & 4: Compare with threshold and trigger alarm
                if distance_cm > 0 and distance_cm < self.distance_threshold_cm:
                    self.alarm.log_event("ALERT", f"Human at {distance_cm:.1f}cm (Threshold: {self.distance_threshold_cm}cm)")
                    self.alarm.trigger_alarm()
                    self.alarm_active = True
                else:
                    self.alarm.stop_alarm()
                    self.alarm_active = False
        else:
            self.alarm.stop_alarm()
            self.alarm_active = False
        
        self.frames_processed += 1
        return detections
    
    def draw_info(self, frame, detections):
        """Draw detection info and statistics on frame"""
        height, width = frame.shape[:2]
        
        # Draw detections
        frame = self.detector.draw_detections(frame, detections, color=(0, 255, 0), thickness=2)
        
        # Draw distance and threshold info
        for det in detections:
            if 'distance_cm' in det:
                distance = det['distance_cm']
                status_color = (0, 0, 255) if distance < self.distance_threshold_cm else (0, 255, 0)
                
                distance_text = f"{distance:.1f}cm"
                cv2.putText(frame, distance_text, 
                           (det['x'] + det['w'] // 2 - 30, det['y'] + det['h'] + 25),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.6, status_color, 2)
        
        # Draw threshold line (visual reference at image center)
        threshold_indicator_y = int(height * 0.5)
        cv2.line(frame, (0, threshold_indicator_y), (width, threshold_indicator_y), 
                (255, 0, 0), 2)
        cv2.putText(frame, f"Threshold: {self.distance_threshold_cm}cm", 
                   (10, threshold_indicator_y - 10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        
        # Draw statistics panel
        stats_text = [
            f"Frames: {self.frames_processed}",
            f"Humans: {self.humans_detected_count}",
            f"Min Distance: {self.min_distance_detected:.1f}cm" if self.min_distance_detected != float('inf') else "Min Distance: -",
            f"Alarm: {'🔴 ACTIVE' if self.alarm_active else '🟢 INACTIVE'}"
        ]
        
        y_offset = 30
        for text in stats_text:
            cv2.putText(frame, text, (10, y_offset),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            y_offset += 25
        
        return frame
    
    def calibrate_distance(self):
        """Interactive calibration for focal length"""
        print("\n📏 Distance Calibration Mode")
        print("Place a person at a known distance in front of camera")
        
        while True:
            ret, frame = self.camera.read_frame()
            if not ret:
                break
            
            detections = self.detector.detect_humans(frame)
            frame = self.detector.draw_detections(frame, detections)
            
            cv2.imshow("Calibration Mode - Press SPACE when ready", frame)
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord(' ') and detections:  # Space pressed
                print(f"Found {len(detections)} human(s)")
                bbox_height = detections[0]['h']
                
                try:
                    known_distance = float(input("Enter distance in cm: "))
                    self.distance_estimator.calibrate_focal_length(known_distance, bbox_height)
                    print("✓ Calibration complete!")
                except ValueError:
                    print("Invalid input")
                break
            elif key == ord('q'):
                break
        
        cv2.destroyWindow("Calibration Mode - Press SPACE when ready")
    
    def run(self):
        """Main run loop"""
        try:
            while True:
                ret, frame = self.camera.read_frame()
                if not ret:
                    print("Failed to read frame")
                    break
                
                # Process frame through detection pipeline
                detections = self.process_frame(frame)
                
                # Draw information on frame
                frame = self.draw_info(frame, detections)
                
                # Display
                cv2.imshow("Human Detection & Alarm System", frame)
                
                # Handle keyboard input
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    print("\n👋 Shutting down...")
                    break
                elif key == ord('r'):
                    print("\n🔄 Resetting statistics...")
                    self.min_distance_detected = float('inf')
                    self.humans_detected_count = 0
                    self.frames_processed = 0
                elif key == ord('c'):
                    self.calibrate_distance()
        
        except KeyboardInterrupt:
            print("\n⚠️  Interrupted by user")
        
        finally:
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        print("\n🧹 Cleaning up...")
        self.alarm.stop_alarm()
        self.camera.release()
        cv2.destroyAllWindows()
        print("✓ Done!")


def main():
    """Main entry point"""
    
    # Configuration
    CAMERA_SOURCE = 0  # Change to IP camera URL if needed
    DISTANCE_THRESHOLD_CM = 200  # Trigger alarm if human is closer than 2 meters
    FOCAL_LENGTH = 1000  # Adjust based on camera calibration
    
    try:
        system = HumanDetectionAlarmSystem(
            camera_source=CAMERA_SOURCE,
            distance_threshold_cm=DISTANCE_THRESHOLD_CM,
            focal_length=FOCAL_LENGTH
        )
        system.run()
    
    except RuntimeError as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
