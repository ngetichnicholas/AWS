import subprocess
import sys

def sync_objects(bucket_name, local_folder, s3_folder, region='us-east-1'):
    # Construct the S3 URI
    s3_uri = f"s3://{bucket_name}/{s3_folder}"

    try:
        # Sync the local folder with the S3 folder
        result = subprocess.run([
            'aws', 's3', 'sync',
            local_folder,
            s3_uri,
            '--region', region
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"Successfully synced {local_folder} to {s3_uri}")
        else:
            print(f"Error syncing {local_folder} to {s3_uri}: {result.stderr}")

    except Exception as e:
        print(f"Failed to sync objects: {e}")

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python sync_objects.py <bucket_name> <local_folder> <s3_folder>")
        sys.exit(1)
    
    bucket_name = sys.argv[1]
    local_folder = sys.argv[2]
    s3_folder = sys.argv[3]
    
    sync_objects(bucket_name, local_folder, s3_folder)
