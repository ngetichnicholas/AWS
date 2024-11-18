## Features
- Automatically triggers when a text file is uploaded to an S3 bucket.
- Counts the number of words in the uploaded text file.
- Sends the word count via email using an SNS topic.
- Optionally supports SMS notifications for the result.
- Provides structured email messages with the subject: **Word Count Result**.

---

## **Prerequisites**
- An **AWS account** with sufficient permissions to create and manage Lambda, S3, and SNS resources.
- An SNS topic with at least one confirmed **email subscription** (and optionally an SMS subscription).
- An S3 bucket for uploading text files.
- **IAM Role**: Ensure you use the `LambdaAccessRole` or a similar role with the following policies:
  - `AWSLambdaBasicExecutionRole`
  - `AmazonSNSFullAccess`
  - `AmazonS3FullAccess`
  - `CloudWatchFullAccess`

---

## Setup Instructions
1. **Create the S3 Bucket**
   - In the AWS Management Console, create an S3 bucket.
   - Note the bucket name for later use.

2. **Create the SNS Topic**
   - In the AWS Management Console, create an SNS topic.
   - Subscribe an email address to the topic and confirm the subscription via the email sent.

3. **Deploy the Lambda Function**
   - Create a new Lambda function in the AWS Management Console using Python as the runtime.
   - Copy the `WordCountFunction.py` function code into the inline editor or upload a ZIP file containing the code.
   - Update the `SNS_TOPIC_ARN` variable with your SNS topic ARN.


4. **Configure S3 Event Trigger**
   - Attach an S3 event trigger to the Lambda function.
   - Configure the trigger to invoke the function for `PUT` events (file uploads).

5. **Deploy and Test**
   - Save and deploy the Lambda function.
   - Upload text files to the S3 bucket to test the functionality.
   - Verify the email notification with the word count.