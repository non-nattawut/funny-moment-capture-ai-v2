import sys
import time
import threading

class UIService:
    def __init__(self):
        self._stop_event = threading.Event()
        self._thread = None

    def _animate(self, message):
        chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        idx = 0
        while not self._stop_event.is_set():
            sys.stdout.write(f"\r{chars[idx % len(chars)]} {message}")
            sys.stdout.flush()
            idx += 1
            time.sleep(0.1)
        sys.stdout.write("\r" + " " * (len(message) + 10) + "\r")
        sys.stdout.flush()

    def start_loading(self, message):
        """Starts a spinner animation in a separate thread."""
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._animate, args=(message,))
        self._thread.start()

    def stop_loading(self):
        """Stops the spinner animation."""
        if self._thread:
            self._stop_event.set()
            self._thread.join()
