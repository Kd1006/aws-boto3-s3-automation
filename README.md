# AWS S3 Automation with Python & Boto3

This project automates basic Amazon S3 operations using **Python**, **Boto3**, **IAM programmatic access**, and the **AWS CLI**.  
It simulates a common cloud-support / cloud-engineer task: managing S3 objects programmatically instead of using the AWS Console.

---

## 🎯 Goal

Use a simple Python script to:

- Upload a file to an S3 bucket
- List objects in the bucket
- Download a file from the bucket
- Delete the file from the bucket
- Confirm that the bucket is empty

Bucket used in this project: **`kd-boto3-demo-bucket`**

---

## 🧰 Technologies Used

- **Amazon S3**
- **AWS IAM** (programmatic user)
- **AWS CLI**
- **Python 3**
- **Boto3** (AWS SDK for Python)
- **macOS Terminal**
- **Virtual environment (`venv`)**

---

## 🛠 Setup & Steps I Followed

### 1️⃣ Created IAM user for programmatic access

- Created a dedicated IAM user for this project
- Attached the **AmazonS3FullAccess** policy (demo only; in real projects I would restrict this to a single bucket)

📸 `screenshots/01-iam-user-boto3-created.png`  
📸 `screenshots/02-iam-user-access-key.png`

---

### 2️⃣ Created S3 bucket

Created an S3 bucket:

- Name: **`kd-boto3-demo-bucket`**
- Region: `us-east-1`
- Block Public Access: all ON (this is not a public website)

📸 `screenshots/03-s3-demo-bucket-created.png`

---

### 3️⃣ Configured AWS CLI

Configured AWS CLI with the IAM user’s access key and secret key:

```bash
aws configure
