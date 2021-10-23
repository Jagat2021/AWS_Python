# Get EC2 instance ID,Image ID and Launchtime AND know how to use strftime() to format date

import boto3
from pprint import pprint

#connect to AWS console
aws_console = boto3.session.Session(profile_name="boto3")

#connect to EC2 console
ec2_console = aws_console.client(service_name="ec2",region_name="us-east-1")

#Function to Get EC2 details
def get_all_ec2_instance_details():
    response = ec2_console.describe_instances()
    for each_item in (response["Reservations"]):
        for each_instance in (each_item["Instances"]):
            print("Instance ID is: {}\tThe Image ID is: {}\t\
            The Launch date is: {}".format(each_instance["InstanceId"],each_instance["ImageId"],each_instance["LaunchTime"].strftime("%d-%m-%y")))

#Define MAIN function
def main():
    get_all_ec2_instance_details()

if __name__ == "__main__":
    main()    