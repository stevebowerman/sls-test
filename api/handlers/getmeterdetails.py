import json
import logging
import os
import boto3
import csv

BUCKET_NAME = os.environ['BUCKET_NAME']
FILE_NAME = os.environ['FILE_NAME']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    status = 400
    response = ""

    try:
        logger.info(event)
        mpan = event["pathParameters"]["mpan"]

        s3 = boto3.client('s3')
        data = s3.get_object(
            Bucket=BUCKET_NAME,
            Key=FILE_NAME
        )["Body"].read().decode('utf-8').split('\n')

        csvdata = list(csv.reader(data))

        match = list(filter(lambda x: x[0] == mpan, csvdata))

        if len(match) > 0:
            response = {
                "mpan":match[0][0],
                "text":match[0][1]
            }
            status = 200
        
        else:
            response = {
                "error":"no match"
            }
            status = 404

    except Exception as e:
        logger.error(e)
        response = {
            "error":str(e)
        }
    

    logger.info(response)

    return {
        "statusCode": status,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True
        },
        "body": json.dumps(response),
        "isBase64Encoded": False
    }