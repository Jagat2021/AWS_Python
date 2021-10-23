# Get AWS account id
import boto3
from pprint import pprint

#aws console connection
aws_console = boto3.session.Session(profile_name="boto3")

#STS console connection
sts_console = aws_console.client(service_name="sts", region_name="us-east-1")

response = sts_console.get_caller_identity()
pprint(response["Account"] + "-->" + response["UserId"])

# Below is using get() method on Dictionary
print(response.get('Account'))
