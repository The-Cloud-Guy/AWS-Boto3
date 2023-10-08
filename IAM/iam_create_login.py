import boto3


def create_login(username):
    iam = boto3.client('iam')

    login_profile = iam.create_login_profile(
        password = 'Mypassword@1',
        passwordResetRequired = False,
        UserName = username
    )

    print(login_profile)



create_login('test')


