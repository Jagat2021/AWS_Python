# Author: Jagat Pradhan
# Disclaimer : Use at your own risk. this is tested in LAB environment
# This script is to create a single bucket in a region and assign a bucket policy

import boto3
import json

# connect to AWS console
aws_console = boto3.session.Session(profile_name="boto3")
# connect to S3
s3_console = aws_console.client(service_name='s3', region_name='us-east-1')

# bucket name
BUCKET_NAME = 'jagat-test-bucket-2021'


def create_bucket(bucket_name):

    s3_console.create_bucket(
        Bucket=bucket_name

    )


def assign_bucket_policy():
    bucket_name = BUCKET_NAME
    bucket_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AddPerm",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:*"],
                "Resource": f'arn:aws:s3:::{bucket_name}/*'
            }
        ]
    }

    policy_string = json.dumps(bucket_policy)

    s3_console.put_bucket_policy(
        Bucket=BUCKET_NAME,
        Policy=policy_string
    )


def main():
    create_bucket(BUCKET_NAME)
    assign_bucket_policy()


if __name__ == '__main__':
    main()
