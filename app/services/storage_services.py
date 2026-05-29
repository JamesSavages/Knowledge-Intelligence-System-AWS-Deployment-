'''
Document Storage for the s3 bucket
'''

import boto3 # AWS service for softward dev
from botocore.exceptions import ClientError
from app import config
from config import Config

class S3Storage:

    def __init__(self):
        
        self.s3 = boto3.client(
            's3',
            aws_access_key_id = Config.AWS_ACCESS_KEY,
            aws_secret_access_key = Config.AWS_SECRET_KEY
        )

