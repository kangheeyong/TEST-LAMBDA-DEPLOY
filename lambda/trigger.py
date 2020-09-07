import json

import boto3

client = boto3.client('stepfunctions')


response = client.start_execution(
        stateMachineArn='arn:aws:states:us-west-2:061182222301:stateMachine:CaseStateMachine-vr6mMJsZKHRt',
        input= json.dumps({11:11})
    )

print(response)