import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "kd-boto3-demo-bucket"
s3 = boto3.client("s3")


def upload_file(local_filename, key):
    print(f"Uploading {local_filename} to s3://{BUCKET_NAME}/{key} ...")
    s3.upload_file(local_filename, BUCKET_NAME, key)
    print("Upload complete")


def list_objects():
    print(f"\nListing objects in bucket {BUCKET_NAME} ...")
    resp = s3.list_objects_v2(Bucket=BUCKET_NAME)
    contents = resp.get("Contents", [])
    if not contents:
        print("Bucket is currently empty.")
    else:
        for obj in contents:
            print(f"- {obj['Key']} ({obj['Size']} bytes)")


def download_file(key, local_filename):
    print(f"\nDownloading {key} to {local_filename} ...")
    s3.download_file(BUCKET_NAME, key, local_filename)
    print("Download complete")


def delete_file(key):
    print(f"\nDeleting {key} ...")
    s3.delete_object(Bucket=BUCKET_NAME, Key=key)
    print("Object deleted")


def main():
    test_key = "hello-from-boto3.txt"
    local_file = "hello-from-boto3.txt"
    downloaded_file = "hello-from-boto3-downloaded.txt"

    # Create a small local file
    with open(local_file, "w") as f:
        f.write("Hello from KD's boto3 S3 automation script!\n")

    try:
        upload_file(local_file, test_key)
        list_objects()
        download_file(test_key, downloaded_file)
        delete_file(test_key)
        list_objects()
    except ClientError as e:
        print("AWS Error:", e)


if __name__ == "__main__":
    main()


