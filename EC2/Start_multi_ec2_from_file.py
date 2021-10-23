# This script will start multiple ec2 taking input from a file

import boto3

#connect to AWS console
aws_console = boto3.session.Session(profile_name="boto3")

#connecto ec2 console
ec2_console = aws_console.client(service_name='ec2',region_name='us-east-1')

# take input from file
instance_list = open("list2.txt", 'r')
content = instance_list.readlines()
print(content)

#format the list to remove the \n line
formated_list = []

# Function to start multiple instance
def start_instances():

    for each_instance in content:
        formated_list.append(each_instance.strip())

    for each_formated_instance in formated_list:
        print('Starting Instance: {}'.format(each_formated_instance))
        ec2_console.start_instances(InstanceIds=[each_formated_instance])
    print("All instances are started. It will take sometime for status checks.")

instance_list.close()

#Define main function
def main():
    start_instances()

if __name__ == "__main__":
    main()    