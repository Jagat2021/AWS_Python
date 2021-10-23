### Get All EC2 Instqance ID ###

import boto3
from pprint import pprint

# AWS console connection
aws_console = boto3.session.Session(profile_name="boto3")

#ec2 console login /ec2 object
ec2_console_client = aws_console.client('ec2',region_name="us-east-1")

#Function to get all instances id
def get_all_instance_id():
    response = ec2_console_client.describe_instances()
    for each_item in response['Reservations'][0]['Instances']:
        pprint(f"Instance ID is:  {each_item['InstanceId']}")

#Define main function
def main():
    get_all_instance_id()  

if __name__ == "__main__":
    main()          

