import boto3
import sys

def delete_bucket(bucket_name):
    s3 = boto3.client('s3')
    
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' deleted.")
    except Exception as e:
        print(f"Error deleting bucket: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python delete_bucket.py <bucket_name>")
        sys.exit(1)
    
    bucket_name = sys.argv[1]
    delete_bucket(bucket_name)
