import boto3
import os
import sys

def put_objects(bucket_name, local_folder, s3_folder, region='us-east-1'):
    s3 = boto3.client('s3', region_name=region)
    
    for filename in os.listdir(local_folder):
        local_file_path = os.path.join(local_folder, filename)
        s3_key = os.path.join(s3_folder, filename)
        
        if os.path.isfile(local_file_path):
            try:
                s3.upload_file(local_file_path, bucket_name, s3_key)
                print(f"Uploaded {local_file_path} to s3://{bucket_name}/{s3_key}")
            except Exception as e:
                print(f"Error uploading {local_file_path}: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python put_objects.py <bucket_name> <local_folder> <s3_folder>")
        sys.exit(1)
    
    bucket_name = sys.argv[1]
    local_folder = sys.argv[2]
    s3_folder = sys.argv[3]
    
    put_objects(bucket_name, local_folder, s3_folder)