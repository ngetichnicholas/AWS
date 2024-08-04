import boto3
import sys

def create_bucket(bucket_name, region='us-east-1'):
    s3 = boto3.client('s3', region_name=region)
    
    # Check if the region is 'us-east-1'
    if region == 'us-east-1':
        # No LocationConstraint needed for 'us-east-1'
        create_bucket_args = {'Bucket': bucket_name}
    else:
        # For other regions, include LocationConstraint
        create_bucket_args = {
            'Bucket': bucket_name,
            'CreateBucketConfiguration': {'LocationConstraint': region}
        }
    
    try:
        s3.create_bucket(**create_bucket_args)
        print(f"Bucket '{bucket_name}' created in region '{region}'.")
    except Exception as e:
        print(f"Error creating bucket: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python create_bucket.py <bucket_name>")
        sys.exit(1)
    
    bucket_name = sys.argv[1]
    create_bucket(bucket_name)