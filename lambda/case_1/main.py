import json
import time
import random


def lambda_handler(event, context):
    t = random.randint(10,60)
    print(f"case 1 -> sleep {t}s")
    print(f'event: {event}')
    print(f'context: {context}')
    time.sleep(t)
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "case_1"
        })
    }
