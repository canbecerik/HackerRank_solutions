# Adapted from https://blog.magrathealabs.com/filesystem-events-monitoring-with-python-9f5329b651c3

import os, time
from watchdog.events import RegexMatchingEventHandler

class FilesEventHandler(RegexMatchingEventHandler):
    """Anytime a pdf is created in script's folder, create an empty py file with the same name"""
    REGEX = [r".*\.pdf$"]

    def __init__(self):
        super().__init__(self.REGEX)

    def on_created(self, event):
        print(f"Detected new PDF file{event.src_path}")

        # Do not proceed until file download has been finished

        # file_size = -1
        # while file_size != os.path.getsize(event.src_path):
        #     file_size = os.path.getsize(event.src_path)
        #     time.sleep(1)
        self.process(event)

    def process(self, event):
        filename, ext = os.path.splitext(event.src_path)
        filename = f"{filename}.py"
        open(filename, 'a').close()
        print(f"Created {filename}.")