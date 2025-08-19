import boto3

aws_management_console = boto3.session.Session(profile_name="default") #loga into management consle

iam_console_resource = aws_management_console.resource("iam") #moves to the iam dashboard

iam_console_client = aws_management_console.client("iam") #client object





for each_user in iam_console_resource.users.all(): #loops through and prints all users
    print(each_user.name)

#iam user list with client object

for each in iam_console_client.list_users()["Users"]:
    print(each["UserName"])


#print(aws_management_console.get_available_resources())

