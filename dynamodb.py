# This file is filled with CRUD operations over a DynamoDB table by the name of "notes".

import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.client('dynamodb', region_name='il-central-1')

# Read (all) operation:
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
        raise Exception('Hmm.. seems like there\'s no notes yet..')


# Read (single) operation:
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
         raise Exception(f'No note with ID of "{note_id}" found.')


# Create (single) operation:
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
        raise Exception('There was an issue creating a note, please try again later.', err)
    
    return response


# Delete (single) operation:
def delete_note(note_id):
    try:
        note = get_note(note_id)
        if(note):
            response = dynamodb.delete_item(
                TableName='notes',
                Key={
                    'note_id': {
                        'S': note_id
                    }   
                })

    except ClientError as err:
        raise Exception(f'There was an issue with deleting the note with the ID of: "{note_id}", please try again later.', err)

    return response


# Update (single) operation:
def update_note(note_id, desc):
    try:
        note = get_note(note_id)
        if(note):
            response = dynamodb.put_item(
            TableName='notes',
            Item={
                'note_id': {
                    'S': note_id
                    },
                'desc': {
                    'S':desc
                    }
                }),


    except ClientError as err:
        raise Exception(f'There was an issue with updating the note with the ID of: "{note_id}", please try again later.', err)

    return response