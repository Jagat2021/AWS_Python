# Author: Jagat Pradhan
# Disclaimer : Use at your own risk. this is tested in LAB environment
# This script is to upload files to S3 bucket

import boto3
from pprint import pprint
import os


# connect to AWS console
aws_console = boto3.session.Session(profile_name="boto3")
# connect to S3 using resource
s3_console = aws_console.resource(service_name='s3')
BUCKET_NAME = input("Enter Bucket name:")
bucket = s3_console.Bucket(BUCKET_NAME)


# function to upload files to s3


def s3_upload_files(path):

    for subdir, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(subdir, file)
            with open(full_path, 'rb') as data:
                bucket.put_object(Key=full_path[len(path)+1:], Body=data)
    print("Upload Completed!")


def main():
    s3_upload_files('/Users/jagat/Desktop/AWS/Python/S3/testfiles')


if __name__ == "__main__":
    main()
