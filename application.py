

# Import necessary packages
import boto3
from flask import Flask, request, jsonify
import json


# Create a S3 client
client = boto3.client('s3')

BUCKET_NAME = 's3-bucket-new-boto3-aws'
# Name of the file with path in S3 bucket
FILE_PATH = 'word.txt'

# Download the file from S3 bucket and save as the same name
client.download_file(BUCKET_NAME, FILE_PATH, FILE_PATH)

# Read the file content
with open(FILE_PATH, 'r') as w:
    m = w.readlines()
    
# Convert the read content to value of a dictionary
m_dict = {"Content String": m}

# Create the flask application
application = Flask(__name__)

# Make the url route
@application.route('/')
def nlp():
    # If the request method is GET return the dict
    if request.method == 'GET':
        return jsonify(m_dict)

    if __name__ == '__main__':
        application.run()