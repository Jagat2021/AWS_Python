# Author: Jagat Pradhan
# Disclaimer : Use at your own risk. this is tested in LAB environment
# This script is to create a single bucket in a region
#

import boto3

# connect to AWS console
aws_console = boto3.session.Session(profile_name="boto3")
# connect to S3
s3_console = aws_console.client(service_name='s3', region_name='us-east-1')

# bucket name
BUCKET_NAME = 'jagat-test-bucket-2021'


def create_bucket(bucket_name):

    s3_console.create_bucket(
        Bucket=bucket_name,
        # CreateBucketConfiguration={
        # if u use 'us-east-1' lcoation validation error wil occur, bcoz it creates bucket in us-east-1 by default.
        # 'LocationConstraint': 'us-east-2'
        # }
    )


def main():
    create_bucket(BUCKET_NAME)


if __name__ == '__main__':
    main()
