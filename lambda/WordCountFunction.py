import json
import boto3

# Create AWS clients
sns = boto3.client('sns')
s3 = boto3.client('s3')

# Replace with your SNS topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:us-west-2:329723857270:WordCountTopic"

def lambda_handler(event, context):
    try:
        # Log the incoming event
        print("Received event:", json.dumps(event))

        # Extract bucket name and file key from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        print(f"Bucket: {bucket_name}, File: {file_key}")

        # Get the text file from S3
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read().decode('utf-8')
        print("File content retrieved successfully.")

        # Count words
        word_count = len(file_content.split())
        print(f"Word count: {word_count}")

        # Prepare message
        message = f"The word count in the file {file_key} is {word_count}."
        subject = "Word Count Result"
        print(f"Prepared message: {message}")

        # Publish message to SNS
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=subject
        )
        print("Message published to SNS.")

        return {
            'statusCode': 200,
            'body': json.dumps(message)
        }

    except Exception as e:
        # Log the error for debugging
        print(f"Error processing file {file_key}: {str(e)}")
        raise
