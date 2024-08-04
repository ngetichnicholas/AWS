# AWS S3 Bash Scripts

This repository contains Bash scripts for managing AWS S3 buckets and objects. The scripts cover creating and deleting buckets, listing buckets and objects, putting objects into buckets, and syncing local directories with S3 buckets.

## Dependencies

Ensure you have the following dependencies installed:

- **AWS CLI**: Command-line tool to manage AWS services.

You can install the AWS CLI using the instructions from the [official AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

## Scripts

### `create-bucket.sh`

Creates an S3 bucket.

**Usage:**

```bash
./create-bucket.sh <bucket_name>
```

**Example:**

```bash
./create-bucket.sh my-new-bucket
```

### `delete-bucket.sh`

Deletes an S3 bucket.

**Usage:**

```bash
./delete-bucket.sh <bucket_name>
```

**Example:**

```bash
./delete-bucket.sh my-old-bucket
```

### `list-buckets.sh`

Lists all S3 buckets.

**Usage:**

```bash
./list-buckets.sh
```

### `list-objects.sh`

Lists all objects in a specified S3 bucket.

**Usage:**

```bash
./list-objects.sh <bucket_name>
```

**Example:**

```bash
./list-objects.sh my-bucket
```

### `put-objects.sh`

Uploads files from a local folder to an S3 bucket, creating random files if necessary.

**Usage:**

```bash
./put-objects.sh <bucket_name> <local_folder>
```

**Example:**

```bash
./put-objects.sh my-bucket local-folder
```

### `sync.sh`

Syncs a local directory with an S3 bucket folder. Uses AWS CLI for the sync operation.

**Usage:**

```bash
./sync.sh <bucket_name> <local_directory>
```

**Example:**

```bash
./sync.sh my-bucket local-directory
```

### `delete-objects.sh`

Deletes specific objects from an S3 bucket, based on the folder structure.

**Usage:**

```bash
./delete-objects.sh <bucket_name> <folder_name>
```

**Example:**

```bash
./delete-objects.sh my-bucket s3-folder
```

## Notes

- Ensure you have AWS credentials configured. You can set up your credentials using the `aws configure` command from the AWS CLI.
- Make sure the scripts have executable permissions. You can grant executable permissions using:

```bash
chmod +x <script_name>.sh
```

## License

This project is licensed under the MIT License. See the [LICENSE](~/LICENSE) file for details.