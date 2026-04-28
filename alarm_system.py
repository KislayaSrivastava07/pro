"""
Alarm System Module
Handles alarm triggering based on threshold violations
"""

import winsound
import threading
from datetime import datetime


class AlarmSystem:
    def __init__(self, alarm_sound_frequency=1000, alarm_sound_duration=500):
        """
        Initialize alarm system
        
        Args:
            alarm_sound_frequency: Frequency of beep in Hz
            alarm_sound_duration: Duration of beep in ms
        """
        self.alarm_sound_frequency = alarm_sound_frequency
        self.alarm_sound_duration = alarm_sound_duration
        self.is_alarming = False
        self.alarm_thread = None
        self.alarm_count = 0
    
    def trigger_alarm(self):
        """Trigger alarm sound (non-blocking)"""
        if not self.is_alarming:
            self.is_alarming = True
            self.alarm_thread = threading.Thread(target=self._alarm_loop, daemon=True)
            self.alarm_thread.start()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"🚨 ALARM TRIGGERED at {timestamp} (Alert #{self.alarm_count + 1})")
            self.alarm_count += 1
    
    def stop_alarm(self):
        """Stop the alarm"""
        if self.is_alarming:
            self.is_alarming = False
            print("✓ Alarm stopped")
    
    def _alarm_loop(self):
        """Internal alarm sound loop"""
        try:
            while self.is_alarming:
                winsound.Beep(self.alarm_sound_frequency, self.alarm_sound_duration)
        except Exception as e:
            print(f"Alarm sound error: {e}")
    
    def log_event(self, event_type, details):
        """Log detection events"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] {event_type}: {details}")
