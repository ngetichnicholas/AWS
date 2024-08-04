# AWS S3 Python Scripts

This repository contains Python scripts for managing AWS S3 buckets and objects. The scripts cover creating and deleting buckets, listing buckets and objects, putting objects into buckets, and syncing local directories with S3 buckets.

## Dependencies

Ensure you have the following dependencies installed:

- **Python 3.x**: Python 3 is required to run the scripts.
- **boto3**: The AWS SDK for Python, used to interact with AWS services.
- **awscli** (optional): For syncing, the AWS CLI is used via subprocess.

You can install the necessary Python dependencies using `pip`:

```bash
pip install boto3
```

## Scripts

### `create_bucket.py`

Creates an S3 bucket.

**Usage:**

```bash
python create_bucket.py <bucket_name>
```

**Example:**

```bash
python create_bucket.py my-new-bucket
```

### `delete_bucket.py`

Deletes an S3 bucket.

**Usage:**

```bash
python delete_bucket.py <bucket_name>
```

**Example:**

```bash
python delete_bucket.py my-old-bucket
```

### `list_buckets.py`

Lists all S3 buckets.

**Usage:**

```bash
python list_buckets.py
```

### `list_objects.py`

Lists all objects in a specified S3 bucket.

**Usage:**

```bash
python list_objects.py <bucket_name>
```

**Example:**

```bash
python list_objects.py my-bucket
```

### `put_objects.py`

Uploads files from a local folder to an S3 bucket.

**Usage:**

```bash
python put_objects.py <bucket_name> <local_folder> <s3_folder>
```

**Example:**

```bash
python put_objects.py my-bucket local-folder s3-folder
```

### `sync_objects.py`

Syncs a local directory with a specified S3 folder. Uses `awscli` for the sync operation.

**Usage:**

```bash
python sync_objects.py <bucket_name> <local_folder> <s3_folder>
```

**Example:**

```bash
python sync_objects.py my-bucket local-folder s3-folder
```

### `delete_objects.py`

Deletes specific objects from an S3 bucket, keeping the folder structure.

**Usage:**

```bash
python delete_objects.py <bucket_name> <s3_folder>
```

**Example:**

```bash
python delete_objects.py my-bucket s3-folder
```

## Notes

- Ensure you have AWS credentials configured. You can set up your credentials using the `aws configure` command from the AWS CLI.
- For `sync_objects.py`, the `awscli` tool must be installed. If not already installed, you can install it with:

```bash
pip install awscli
```

## License

This project is licensed under the MIT License. See the [LICENSE](~/LICENSE) file for details.
