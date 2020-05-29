# Adapted from https://blog.magrathealabs.com/filesystem-events-monitoring-with-python-9f5329b651c3

import sys, os, subprocess
import time

from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler

class FilesWatcher:
    def __init__(self, src_path):
        self.__src_path = src_path
        self.__event_handler = FilesEventHandler()
        self.__event_observer = Observer()

    def run(self):
        self.start()
        print(f"FilesWatcher is now running, will create {curr_extension.upper()} files.")
        # print(f"FilesWatcher is now running, will create {sys.argv[1].upper()} files.")
        print("Press CTRL+C to terminate.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Received CTRL+C, terminating...")
            self.stop()

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()
        print("Watcher terminated.")

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=True
        )

class FilesEventHandler(RegexMatchingEventHandler):
    """Anytime a pdf is created in script's folder, create an empty file with the same name and given extension as CL argument"""
    REGEX = [r".*\.pdf$"]

    def __init__(self):
        super().__init__(self.REGEX)

    def on_created(self, event):
        print(f"\nDetected new PDF file:\n{event.src_path}")

        # Do not proceed until file download has been finished

        # file_size = -1
        # while file_size != os.path.getsize(event.src_path):
        #     file_size = os.path.getsize(event.src_path)
        #     time.sleep(1)
        self.process(event)

    def process(self, event):
        filename = os.path.splitext(event.src_path)[0]
        # extension = sys.argv[1] if len(sys.argv) > 1 else 'py'
        extension = curr_extension.lower()
        filename = f"{filename}.{extension}"
        open(filename, 'a').close()
        print()
        print(f"Created {filename}.")
        subprocess.Popen(f"code -r {filename}" if editor == 1 else filename, shell=True)
 
if __name__ == "__main__":
    # if len(sys.argv) == 1:
    #     print("Usage: watcher.py <extension> <optional_path>")
    #     print("Example: watcher.py json")
    #     exit()
    # src_path = sys.argv[2] if len(sys.argv) > 2 else '.'
    os.system('cls' if os.name == 'nt' else 'clear')
    # Get required configuration
    allowed_extensions = {
        "SQL" : {"extension" : 'SQL', "path": "Specialized_Skills\SQL"},
        "PY" : {"extension" : 'PY', "path": "Language_Proficiency\Python"},
        "C" : {"extension" : 'C', "path": "Language_Proficiency\C"},
        "CPP" : {"extension" : 'CPP', "path": "Language_Proficiency\C++"}
    }
        
    curr_extension = input("Enter extension: ").upper()
    # src_path = ('.' if src_path == "" else src_path)
    if curr_extension not in allowed_extensions:
        print("Error: extension not supported. Supported extensions are:")
        [print(i) for i in allowed_extensions]
        print()
        print("Terminating watcher...")
        exit()
    else:
        src_path = allowed_extensions[curr_extension]["path"]
    editor = int(input("Select Editor:\n[1]- VSCode\n[2]- Default System Editor\n> "))

    print("Launching Watcher...\n")
    FilesWatcher(src_path).run()
