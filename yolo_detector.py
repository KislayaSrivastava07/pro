"""
YOLO Human Detection Module
Detects humans using YOLOv8
"""

from ultralytics import YOLO
import cv2


class YOLODetector:
    def __init__(self, model_name='yolov8n.pt', confidence_threshold=0.5):
        """
        Initialize YOLO detector
        
        Args:
            model_name: YOLO model to use ('yolov8n', 'yolov8s', 'yolov8m', 'yolov8l')
            confidence_threshold: Detection confidence threshold
        """
        self.model = YOLO(model_name)
        self.confidence_threshold = confidence_threshold
        self.HUMAN_CLASS_ID = 0  # Class ID 0 is always 'person' in COCO dataset
    
    def detect_humans(self, frame):
        """
        Detect humans in frame
        
        Args:
            frame: Input frame (BGR)
            
        Returns:
            List of detections with format: [(x, y, w, h, confidence), ...]
        """
        results = self.model(frame, conf=self.confidence_threshold, verbose=False)
        
        detections = []
        for result in results:
            for box in result.boxes:
                # Filter only humans (class_id = 0)
                if int(box.cls) == self.HUMAN_CLASS_ID:
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    confidence = box.conf[0].cpu().numpy()
                    
                    x = int(x1)
                    y = int(y1)
                    w = int(x2 - x1)
                    h = int(y2 - y1)
                    
                    detections.append({
                        'x': x,
                        'y': y,
                        'w': w,
                        'h': h,
                        'confidence': float(confidence)
                    })
        
        return detections
    
    def draw_detections(self, frame, detections, color=(0, 255, 0), thickness=2):
        """
        Draw bounding boxes on frame
        
        Args:
            frame: Input frame
            detections: List of detections
            color: Box color (BGR)
            thickness: Line thickness
            
        Returns:
            Frame with drawn boxes
        """
        for det in detections:
            x = det['x']
            y = det['y']
            w = det['w']
            h = det['h']
            conf = det['confidence']
            
            # Draw rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)
            
            # Draw confidence text
            label = f"Person {conf:.2f}"
            cv2.putText(frame, label, (x, y - 10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        return frame
