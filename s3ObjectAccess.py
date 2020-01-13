"""
    The object is assumed to be a file in and already created s3 bucket and is read directly using boto3 client.
    Pre-requisites: AWS account, an S3 bucket containing a file with some data.
"""
import boto3    #Python lib to interact with AWS services

s3_client = boto3.client('s3')
bucket_name = 'azhertestbucket'     #bucket name to access, should be changed accordingly
fileKey = 'testfile.txt'            #bucket file to be access, should be changed accordingly

obj = s3_client.get_object(
    Bucket = bucket_name,
    Key = fileKey
)

filedata = obj['Body'].read().decode('UTF-8')       #read file data and decode

print(filedata)

