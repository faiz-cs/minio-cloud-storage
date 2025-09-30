import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from minio import Minio

client = Minio(
    "your-vm-ip:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

bucket_name = "mybucket"
folder_path = "/home/ubuntu/files_to_upload"

if not client.bucket_exists(bucket_name):
    client.make_bucket(bucket_name)

class UploadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            filename = os.path.basename(event.src_path)
            try:
                client.fput_object(bucket_name, filename, event.src_path)
                print(f"✅ Uploaded immediately: {filename}")
            except Exception as e:
                print(f"❌ Upload failed: {e}")

event_handler = UploadHandler()
observer = Observer()
observer.schedule(event_handler, folder_path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
