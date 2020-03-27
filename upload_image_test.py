import boto3
from botocore.exceptions import NoCredentialsError
import string
import random


def upload_to_aws(local_file, s3_file_name):
    BUCKET = 'lowballimages'

    s3 = boto3.client('s3', profile_name='default', region_name='us-east-2')

    try:
        s3.upload_file(local_file, BUCKET, s3_file_name)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def randomstring(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def main():
    print("Start")
    upload_to_aws('C:/Users/grigg/Downloads/test_image_2.jpeg', "test_image_2")
    print("done")

main()