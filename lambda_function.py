import urllib.request
import time
import json
from datetime import datetime, timezone
from decimal import Decimal
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("network-monitor-results")


def lambda_handler(event, context):

    host = event.get("queryStringParameters", {}).get(
        "host", "example.com"
    )

    url = "https://" + host

    try:
        start = time.time()

        response = urllib.request.urlopen(url, timeout=5)

        end = time.time()

        response_time = Decimal(
            str(round((end - start) * 1000, 2))
        )

        status = "UP"

    except Exception:
        response_time = None
        status = "DOWN"

    timestamp = datetime.now(timezone.utc).isoformat()

    # Store result in DynamoDB
    table.put_item(
        Item={
            "id": timestamp,
            "host": host,
            "status": status,
            "response_time_ms": response_time
        }
    )

    # Return result as JSON
    result = {
        "host": host,
        "status": status,
        "response_time_ms": (
            float(response_time)
            if response_time is not None
            else None
        ),
        "timestamp": timestamp
    }

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(result)
    }