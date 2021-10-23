# Get all IAM users listing
import boto3
from pprint import pprint

# login to console
aws_connection = boto3.session.Session(profile_name="boto3")

# open IAM console
iam_console = aws_connection.client('iam')
# pprint(dir(iam_console))

# Function to list all user using list_users method
def get_all_iam_users():
    all_iam_users = iam_console.list_users()
    for each_user in all_iam_users["Users"]:
        pprint(each_user["UserName"])

# Define MAIN function
def main():
    get_all_iam_users()        

# call to main function
if __name__ == "__main__":
    main()