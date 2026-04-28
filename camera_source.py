"""
Camera Source Module
Handles webcam and IP camera frame capture
"""

import cv2


class CameraSource:
    def __init__(self, source=0):
        """
        Initialize camera source
        
        Args:
            source: 0 for webcam, or URL for IP camera (e.g., 'http://192.168.1.100:8080/video')
        """
        self.cap = cv2.VideoCapture(source)
        self.source = source
        self.frame_count = 0
        
        if not self.cap.isOpened():
            raise RuntimeError(f"Cannot open camera source: {source}")
        
        # Set frame properties
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
    
    def read_frame(self):
        """
        Read next frame from camera
        
        Returns:
            Tuple (success, frame) - frame is None if unsuccessful
        """
        ret, frame = self.cap.read()
        if ret:
            self.frame_count += 1
        return ret, frame
    
    def get_fps(self):
        """Get frames per second"""
        return self.cap.get(cv2.CAP_PROP_FPS)
    
    def get_frame_size(self):
        """Get frame dimensions"""
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return width, height
    
    def release(self):
        """Release camera resource"""
        self.cap.release()
    
    def __del__(self):
        self.release()
