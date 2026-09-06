# Cloud Network Monitor

A serverless AWS application that monitors host availability and HTTP response time.

## Architecture

User → API Gateway → AWS Lambda → DynamoDB

CloudWatch is used for logging and monitoring.

## AWS Services Used

- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

## Technologies

- Python 3.10
- HTTP/HTTPS
- JSON
- Boto3

## How It Works

1. The user sends a target host through an HTTP request.
2. API Gateway receives the request.
3. API Gateway invokes the Lambda function.
4. Lambda performs an HTTP/HTTPS connectivity check.
5. Lambda measures the response time.
6. The host is classified as UP or DOWN.
7. The result is stored in DynamoDB with a timestamp.
8. The result is returned to the user as JSON.

## Example Response

{
  "host": "google.com",
  "status": "UP",
  "response_time_ms": 120.5,
  "timestamp": "2026-09-03T..."
}

## IAM

The Lambda execution role is configured with least-privilege permissions to store monitoring results in DynamoDB.

## Monitoring

CloudWatch Logs are used to monitor Lambda executions and troubleshoot errors.

## Project Purpose

This project was built as a hands-on learning project to practice AWS serverless architecture, cloud networking concepts, IAM permissions, API integration, and database storage.
