import boto3
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

aws_session = boto3.session.Session(
    region_name=os.environ.get("AWS_REGION"),
    aws_access_key_id=os.environ.get("AWS_SECRET_ACCESS_ID"),
    aws_secret_access_key=os.environ.get("AWS_ACCESS_KEY_KEY"),
)
sqs = aws_session.resource('sqs')
sqs_queue = sqs.Queue(os.environ.get("AWS_QUEUE_URL"))
