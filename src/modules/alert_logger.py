from typing import Any


class AlertLogger:
    """Stores detection results and generates alerts."""

    def log_detection(self, detection: Any) -> None:
        """Store a detection result."""
        pass

    def generate_alert(self, detection: Any) -> str:
        """Generate an alert for a detected event."""
        pass

    def save_log(self, message: str) -> None:
        """Save an event message to the log."""
        pass