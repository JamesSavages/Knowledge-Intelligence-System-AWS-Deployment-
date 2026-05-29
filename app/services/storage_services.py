'''
Document Storage for the s3 bucket
'''

import boto3 # AWS service for softward dev
from botocore.exceptions import ClientError
from botocore.retries import bucket
from sqlalchemy import exc
from urllib3 import response
# from app import config
from config import Config

class S3Storage:

    def __init__(self):
        
        self.s3 = boto3.client(
            's3',
            aws_access_key_id = Config.AWS_ACCESS_KEY,
            aws_secret_access_key = Config.AWS_SECRET_KEY
        )

        self.bucket = Config.AWS_BUCKET_NAME


    def upload_file(self, file_object, file_name):
        try:
            self.s3.upload_fileobj(file_object, self.bucket, file_name)
            return True
        except ClientError as e:
            print(f"Error uploading file: {e}")
            return

    def get_file(self, filename):
        try:
            reponse = self.s3.get_object(Bucket=self.bucket, Key=filename)
            return response['Body']
        except ClientError as e:
            print(f"Error retrieving file: {e}")
            return None 
