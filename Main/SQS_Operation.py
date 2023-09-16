import boto3
import json
from Helper import mask_data

sqs_client = boto3.client(
    'sqs',
    region_name='us-east-1',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test'
)

queue_url = 'http://localhost:4566/000000000000/login-queue'

def read_messages_from_queue():
    from DatabaseOperations import store_data_in_postgres  # Import here to prevent circular dependency

    response = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=2
    )

    if 'Messages' in response:
        for message in response['Messages']:
            data = json.loads(message['Body'])
            
            if 'device_id' in data:
                data['masked_device_id'] = mask_data(data['device_id'])
            if 'ip' in data:
                data['masked_ip'] = mask_data(data['ip'])

            store_data_in_postgres(data)

            sqs_client.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )
    else:
        print("No messages available in the queue.")
