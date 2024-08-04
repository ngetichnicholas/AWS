import boto3
import sys

def delete_objects(bucket_name, s3_folder, region='us-east-1'):
    s3 = boto3.client('s3', region_name=region)
    
    try:
        result = s3.list_objects_v2(Bucket=bucket_name, Prefix=s3_folder)
        if 'Contents' in result:
            for obj in result['Contents']:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                print(f"Deleted s3://{bucket_name}/{obj['Key']}")
        else:
            print(f"No objects found in {s3_folder}")
    except Exception as e:
        print(f"Error deleting objects: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python delete_objects.py <bucket_name> <s3_folder>")
        sys.exit(1)
    
    bucket_name = sys.argv[1]
    s3_folder = sys.argv[2]
    
    delete_objects(bucket_name, s3_folder)
