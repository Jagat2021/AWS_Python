# Stop multiple EC2 instance taking input from a file
import boto3

#Connect to AWS console
aws_console = boto3.session.Session(profile_name="boto3")

#Connect to EC2 console
ec2_console = aws_console.client(service_name="ec2",region_name="us-east-1")

# Read the file for each instance to apply loop
instance_list = open("list.txt", "r")
content = instance_list.readlines()

#Empty list to keep formated instance id list by removing the "\n" which comes by default
formated_list = []

# Function to stop instances
def stop_instances():
    for each_item in content:
        formated_list.append(each_item.strip())  # to remove the \n from end of each item in the list


    for each_formated_item in formated_list:
        print("Stopping instance: {}".format(each_formated_item))
        ec2_console.stop_instances(InstanceIds=[each_formated_item])
    print("All instances are stopped. Please check")   
    
#Define main funtion
def main():
    stop_instances()

if __name__ == "__main__":
    main()

instance_list.close()