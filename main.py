import boto3

aws_management_console = boto3.session.Session(profile_name="default") #loga into management consle

iam_console = aws_management_console.resource("iam") #moves to the iam dashboard

for each_user in iam_console.users.all(): #lopps through and prints all users
    print(each_user.name)
