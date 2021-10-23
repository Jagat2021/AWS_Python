# Get to know how waiters work while working with EC2
import boto3
import sys

# Connect to AWS mgmt console
aws_console = boto3.session.Session(profile_name="boto3")
# Connect to ec2 console
ec2_console = aws_console.client(service_name='ec2', region_name='us-east-1')

while True:
    instance_id = input("Enter the instance ID: ")
    print("Starting the instance: {}".format(instance_id))
    ec2_console.start_instances(InstanceIds=[instance_id])

    # waiter implementation
    waiter = ec2_console.get_waiter('instance_running')
    waiter.wait(InstanceIds=[instance_id])

    print("Your instance: {} is running now".format(instance_id))
    sys.exit()
