from minio import Minio

client = Minio(
    "your-vm-ip:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

client.fput_object("mybucket", "test.txt", "test.txt")
print("File uploaded successfully!")
