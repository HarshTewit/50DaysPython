import os 
import shutil 
from watchdog.events import FileSystemEventHandler 
from watchdog.observers import Observer 

WATCH_FOLDER = os.path.expanduser("~/Downloads")

FILE_DEST = { 
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.png': 'Images'
}

class FileMoverHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return 
        
        filepath = event.src_path
        ext = os.path.splitext(filepath)[1].lower()

        dest_folder = FILE_DEST.get(ext, 'Others')
        full_dest = os.path.join(WATCH_FOLDER, dest_folder)
        os.makedirs(full_dest, exist_ok = True)
        move_to = os.path.join(full_dest, os.path.basename(filepath))

        try:
            shutil.move(filepath, move_to)
        except:
            print("Failed to move.")

            #now somebody has to listen to this event 

if __name__ == "__main__":
    print(f"Watching folder: {WATCH_FOLDER}")
    event_handler = FileMoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursice=False)
    observer.start()

    try:
        while True:
            pass 
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    
