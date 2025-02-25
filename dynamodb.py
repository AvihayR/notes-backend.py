import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb', region_name='il-central-1')


def get_notes():
    try:
        response = dynamodb.scan(
                TableName='notes',
                )
    except ClientError as err:
        print('There was an issue getting notes, try again later', err)
    else:
        return response['Items']

