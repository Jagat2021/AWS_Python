# Get Volume details available in a region
import boto3
from pprint import pprint

# connect to AWS console
aws_console = boto3.session.Session(profile_name="boto3")
# create ec2 console connection
ec2_console = aws_console.client(service_name='ec2', region_name='us-east-1')

# Function to get volume detaiols


def get_volume_imventory():
    response = ec2_console.describe_volumes()
    for each_volume in response["Volumes"]:

        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(each_volume['VolumeId'], each_volume['State'], each_volume['AvailabilityZone'], each_volume[
              'VolumeType'], each_volume["Iops"], each_volume['CreateTime'].strftime("%y-%m-%d"), each_volume['Attachments'][0]['InstanceId']))

# Define main function


def main():
    get_volume_imventory()


if __name__ == "__main__":
    main()
