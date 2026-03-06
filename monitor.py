import logging
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configure logging to both a file and the console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("file_monitor.log"), # Saves to this file
        logging.StreamHandler()                 # Also prints to terminal
    ]
)

class MonitorHandler(FileSystemEventHandler):
    def on_created(self, event):
        logging.info(f"CREATED: {event.src_path}")

    def on_moved(self, event):
        logging.info(f"MOVED/COPIED: from {event.src_path} to {event.dest_path}")

if __name__ == "__main__":
    path = "." 
    event_handler = MonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    logging.info(f"Monitoring started on: {path}")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()