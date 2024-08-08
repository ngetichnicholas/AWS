## Create a bucket

```sh
aws s3api create-bucket \
--bucket policybucket231 \
--region us-east-1
```

## Create a policy

```sh
aws s3api put-bucket-policy \
--bucket policybucket231 \
--policy file://policy.json
```
