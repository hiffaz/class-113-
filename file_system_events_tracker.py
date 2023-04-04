import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):
    def on_created (self ):
        print("filecreated")

    #1_on_created
    def on_deleted(self):
        print("filecreated")
    def on_modified(self):
        print("filecreated")
    def on_moved(self):
        print("filecreated")
    #2_on_deleted

    #3_on_modified

    #4_on_moved

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt

while True:
    time.sleep(2)
    print("running...")






