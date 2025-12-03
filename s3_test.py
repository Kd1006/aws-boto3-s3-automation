import boto3

bucket_name = "kd-boto3-demo-bucket"
file_name = "hello-from-boto3.txt"
download_file = "downloaded-hello.txt"

s3 = boto3.client("s3")

def list_bucket():
    print(f"\nListing objects in bucket {bucket_name} ...")
    response = s3.list_objects_v2(Bucket=bucket_name)
    if "Contents" not in response:
        print("🪣 Bucket is currently empty.")
    else:
        for obj in response["Contents"]:
            print(" -", obj["Key"])

print("Uploading file...")
s3.put_object(Bucket=bucket_name, Key=file_name, Body="Hello from Boto3!")

print("Download complete")
s3.download_file(bucket_name, file_name, download_file)

print("Deleting file...")
s3.delete_object(Bucket=bucket_name, Key=file_name)

print("Object deleted")
list_bucket()

