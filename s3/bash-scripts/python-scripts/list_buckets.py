import boto3
import sys

def list_buckets():
    s3 = boto3.client('s3')
    
    try:
        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        print("Buckets:")
        for bucket in buckets:
            print(bucket)
    except Exception as e:
        print(f"Error listing buckets: {e}")
        sys.exit(1)

if __name__ == '__main__':
    list_buckets()
