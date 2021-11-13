# Author: Jagat Pradhan
# Disclaimer : Use at your own risk. this is tested in LAB environment
# This script is to list buckets in a AWS account

import boto3


# connect to AWS console
aws_console = boto3.session.Session(profile_name='boto3')

# connect to S3 console
s3_console = aws_console.client(service_name='s3')


def list_objects():
    BUCKET_NAME = input("Enter the bucket name:")
    response = s3_console.list_objects(
        Bucket=BUCKET_NAME
    )
    for each_item in (response['Contents']):
        print(each_item['Key'])


def main():
    list_objects()


if __name__ == "__main__":
    main()
