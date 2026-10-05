from typing import Any


class ImagePreprocessor:
    """Prepares input images for AI model inference."""

    def resize(self, frame: Any, width: int, height: int) -> Any:
        """Resize an image frame."""
        pass

    def normalize(self, frame: Any) -> Any:
        """Normalize image values."""
        pass

    def preprocess(self, frame: Any) -> Any:
        """Perform complete preprocessing."""
        pass