import boto3

s3 = boto3.client("s3")
BUCKET = "kd-boto3-demo-bucket"
FILE_NAME = "hello-from-boto3.txt"
LOCAL_DOWNLOAD = "downloaded-hello.txt"

print("Uploading file...")
s3.put_object(
    Bucket=BUCKET,
    Key=FILE_NAME,
    Body=b"Hello from Boto3 automation!"
)
print("Upload complete ✔️")

print("\nListing objects...")
resp = s3.list_objects_v2(Bucket=BUCKET)
for obj in resp.get("Contents", []):
    print(" -", obj["Key"])

print("\nDownloading file...")
with open(LOCAL_DOWNLOAD, "wb") as f:
    s3.download_fileobj(BUCKET, FILE_NAME, f)
print("Download complete ✔️")

print("\nDeleting file...")
s3.delete_object(Bucket=BUCKET, Key=FILE_NAME)
print("Object deleted ✔️")

print("\nListing objects after deletion...")
resp = s3.list_objects_v2(Bucket=BUCKET)
if "Contents" not in resp:
    print("Bucket is empty ✔️")
else:
    print("Remaining objects:", resp["Contents"])


