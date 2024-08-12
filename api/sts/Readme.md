## Create a user with no permissions

We need to create a new user with no permissions and generate access keys

```sh
aws iam create-user --user-name nick-machine-sts
aws iam create-access-key --user-name nick-machine-sts --output table
```

copy the access key and secret here

```sh
aws configure
```

Then edit credentials file to change from default profile to something different(i.e sts)

```sh
sudo nano ~/.aws/credentials
```

Test who you are:

```sh
aws sts get-caller-identity --profile sts
```
Make sure you don't have access to s3 

```sh
aws s3 ls --profile sts
```
Output: An error occurred (AccessDenied) when calling the ListBuckets operation: Access Denied


## Create a role
 
We need to create a role that will access a new resource

```sh
chmod u+x bin/deploy.sh
./bin/deploy.sh
```

## Use new user credentials and assume role

```sh
aws iam put-user-policy \
    --user-name nick-machine-sts \
    --policy-name StsAssumePolicy \
    --policy-document file://policy.json
```

```sh
aws sts assume-role \
--role-arn "arn:aws:iam::150518037113:role/my-sts-fun-stack-StsRole-LqNukCRRU9dJ" \
--role-session-name s3-sts-session \
--profile sts
```

```sh
aws sts get-caller-identity --profile assumed
```

```sh
 aws s3 ls --profile assumed
 ```