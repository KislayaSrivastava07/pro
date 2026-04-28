"""
Distance Estimation Module
Estimates distance to detected humans based on bounding box dimensions
"""

import numpy as np
import cv2


class DistanceEstimator:
    def __init__(self, focal_length=1000, known_height=170):
        """
        Initialize distance estimator
        
        Args:
            focal_length: Camera focal length (in pixels) - calibrate with your camera
            known_height: Average human height in cm (default: 170cm)
        """
        self.focal_length = focal_length
        self.known_height = known_height
    
    def estimate_distance(self, bbox_height):
        """
        Estimate distance using the focal length method
        Formula: Distance = (known_height * focal_length) / bbox_height
        
        Args:
            bbox_height: Height of bounding box in pixels
            
        Returns:
            Distance in centimeters (or -1 if invalid)
        """
        if bbox_height <= 0:
            return -1
        
        distance_cm = (self.known_height * self.focal_length) / bbox_height *0.5
        return distance_cm
    
    def estimate_distance_meters(self, bbox_height):
        """Returns distance in meters"""
        distance_cm = self.estimate_distance(bbox_height)
        if distance_cm == -1:
            return -1
        return distance_cm / 100
    
    def calibrate_focal_length(self, known_distance_cm, bbox_height_at_distance):
        """
        Calibrate focal length if you know distance and bbox height
        
        Args:
            known_distance_cm: Known distance to object in cm
            bbox_height_at_distance: Bounding box height at that distance
        """
        if bbox_height_at_distance > 0:
            self.focal_length = (known_distance_cm * bbox_height_at_distance) / 170
            print(f"Focal length calibrated to: {self.focal_length}")
