## Create a NACL

```sh
aws ec2 create-network-acl \
--vpc-id vpc-0e1a58e859f306be3
```

## Add entry

```sh
aws ec2 create-network-acl-entry \
--network-acl-id acl-0b9fe0eac00c7f664 \
--ingress \
--rule-number 90 \
--protocol -1 \
--port-range From=0,To=65535 \
--cidr-block 41.90.64.13/32 \
--rule-action deny
```


## Get AMI for Amazon Linux 2

```sh
aws ec2 describe-images \
--owners amazon \
--filters "Name=name,Values=amzn2-ami-hvm-*-x86_64-gp2" "Name=state,Values=available" \
--query "Images[?starts_with(Name, 'amzn2')]|sort_by(@, &CreationDate)[-1].ImageId" \
--region us-east-1 \
 --output text
```