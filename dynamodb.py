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
        return
        
    if 'Items' in response:
        return response['Items']
    else:
        return f'Hmm.. seems like there\'s no notes yet.. please try again later'


def get_note(note_id):
    try:
        response = dynamodb.get_item(
            TableName='notes',
            Key={
                'note_id': {
                    'S': note_id
                }
            })
    
    except ClientError as err:
        print(f'There was an issue getting note with the ID of: {note_id}, please try again later.', err)
        return

    if 'Item' in response:
        return response["Item"]
    else:
        return f'No note with ID of "{note_id}" found.'


def create_note(note_id, desc):
    try:
        response = dynamodb.put_item(
            TableName='notes',
            Item={
                'note_id': {
                    'S': note_id
                    },
                'desc': {
                    'S':desc
                    }
            })
    
    except ClientError as err:
        print('There was an issue creating a note, please try again later.', err)
        return
    
    print(response)
    return response