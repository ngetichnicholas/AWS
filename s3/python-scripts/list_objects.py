import boto3
import sys

def list_objects(bucket_name):
    s3 = boto3.client('s3')
    
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            objects = [obj['Key'] for obj in response['Contents']]
            print("Objects:")
            for obj in objects:
                print(obj)
        else:
            print("No objects found.")
    except Exception as e:
        print(f"Error listing objects: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python list_objects.py <bucket_name>")
        sys.exit(1)
    
    bucket_name = sys.argv[1]
    list_objects(bucket_name)
