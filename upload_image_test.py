import boto3
from botocore.exceptions import NoCredentialsError
import string
import random


def upload_to_aws(local_file, s3_file_name):
    ACCESS_KEY = 'AKIAIOQISPXCU4ZTULGA'
    SECRET_KEY = '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'
    BUCKET = 'lowballimages'

    s3 = boto3.client('s3', ACCESS_KEY, SECRET_KEY)

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


