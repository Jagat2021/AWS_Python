# start single EC2 instance from user input
import boto3
import sys

# Connect to AWS mgmt console
aws_console = boto3.session.Session(profile_name="boto3")
# Connect to ec2 console
ec2_console = aws_console.client(service_name='ec2', region_name='us-east-1')

# Function to start the EC2
while True:
    instance_id = input("Enter the Instance ID to start: ")
    print("Starting the Instance....")
    
    #Start the instance using client method
    ec2_console.start_instances(InstanceIds=[instance_id])

    #Configure waiter untill ec2 state=running
    waiter=ec2_console.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])

    print("Now your instance: {} is in running state".format(instance_id))

    sys.exit()