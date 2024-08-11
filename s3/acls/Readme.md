## Create a bucket

```sh
aws s3api create-bucket \
--bucket aclsbucket231 \
--region us-east-1
```

## Turn off Block Public Access for ACLs

```sh
aws s3api put-public-access-block \
--bucket aclsbucket231 \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```

## Change bucket ownership

```sh
aws s3api put-bucket-ownership-controls \
    --bucket aclsbucket231 \
    --ownership-controls="Rules=[{ObjectOwnership=BucketOwnerPreferred}]"
```