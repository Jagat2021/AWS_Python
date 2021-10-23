#Author: Jagat Pradhan
# Disclaimer : Use at your own risk. this is tested in LAB environment
# This script is to get all RUNNING ec2 instances

# Import boto3 module
import boto3

# connect to AWS mgmt console
aws_console = boto3.session.Session(profile_name="boto3")

#connect to ec2 console
ec2_console = aws_console.resource(service_name="ec2",region_name="us-east-1")

#Function to get all stopped instances
def get_running_instances():

    #filter variable
    running_instance = {"Name": "instance-state-name","Values": ["running"]}

    n=1
    for each_item in ec2_console.instances.filter(Filters=[running_instance]):
        print(n," ",each_item.tags[0]["Value"]," ",each_item.instance_id,each_item.state['Name'])
        n=n+1

def main():
    get_running_instances()

if __name__ == "__main__":
    main()    