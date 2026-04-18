import json
import os
from pathlib import Path


class Storage:
    def __init__(self):
        self.data_dir = Path.home() / ".timelogger"
        self.data_dir.mkdir(exist_ok=True)
        self.data_file = self.data_dir / "data.json"
        self.settings_file = self.data_dir / "settings.json"
        self.data = self._load_data()
        self.settings = self._load_settings()
    
    def _load_data(self):
        if self.data_file.exists():
            try:
                with open(self.data_file, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {"activities": []}
        return {"activities": []}
    
    def _load_settings(self):
        if self.settings_file.exists():
            try:
                with open(self.settings_file, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return {"window_position": None, "always_on_top": False}
        return {"window_position": None, "always_on_top": False}
    
    def save_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.data, f, indent=2)
    
    def save_settings(self):
        with open(self.settings_file, "w") as f:
            json.dump(self.settings, f, indent=2)
    
    def get_activities(self):
        return self.data.get("activities", [])
    
    def add_activity(self, name, color):
        activities = self.data.get("activities", [])
        existing = next((a for a in activities if a["name"].lower() == name.lower()), None)
        if existing:
            return existing
        activity = {"name": name, "color": color, "total_seconds": 0}
        activities.append(activity)
        self.data["activities"] = activities
        self.save_data()
        return activity
    
    def add_time(self, name, seconds):
        activities = self.data.get("activities", [])
        for activity in activities:
            if activity["name"].lower() == name.lower():
                activity["total_seconds"] = activity.get("total_seconds", 0) + seconds
                self.save_data()
                return
        activity = {"name": name, "color": "#888888", "total_seconds": seconds}
        activities.append(activity)
        self.data["activities"] = activities
        self.save_data()
    
    def get_activity_color(self, name):
        activities = self.data.get("activities", [])
        for activity in activities:
            if activity["name"].lower() == name.lower():
                return activity.get("color", "#888888")
        return "#888888"
    
    def get_window_position(self):
        return self.settings.get("window_position")
    
    def set_window_position(self, x, y):
        self.settings["window_position"] = {"x": x, "y": y}
        self.save_settings()
    
    def get_always_on_top(self):
        return self.settings.get("always_on_top", False)
    
    def set_always_on_top(self, value):
        self.settings["always_on_top"] = value
        self.save_settings()