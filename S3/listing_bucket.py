# Author: Jagat Pradhan
# Disclaimer : Use at your own risk. this is tested in LAB environment
# This script is to list buckets in a AWS account

import boto3
from pprint import pprint

# connect to AWS console
aws_console = boto3.session.Session(profile_name='boto3')

# connect to S3 console
s3_console = aws_console.client(service_name='s3')


def list_all_bucket():
    response = s3_console.list_buckets()
    for each_item in (response.get('Buckets')):
        print(each_item['Name'])


def main():
    list_all_bucket()


if __name__ == "__main__":
    main()
