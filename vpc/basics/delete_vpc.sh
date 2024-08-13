#!/usr/bin/env bash

## Delete VPC 

echo "==delete vpc=="
# Check for vpc id
if [ -z "$1" ]; then
    echo "There need to be a vpc-id"
    exit 1
else
    export VPC_ID="$1"
fi

if [ -z "$2" ]; then
  echo "There need to be IGW ID."
else
  export IGW_ID="$2"
fi

if [ -z "$3" ]; then
  echo "There need to be subnet id."
else
  export SUBNET_ID="$3"
fi

if [ -z "$4" ]; then
  echo "ASSOC_ID not provided."
else
  export ASSOC_ID="$4"
fi

if [ -z "$5" ]; then
  echo "RT_ID not provided."
else
  export RT_ID="$5"
fi


# detach the IGW
aws ec2 detach-internet-gateway --internet-gateway-id $IGW_ID --vpc-id $VPC_ID

# delete the IGW
aws ec2 delete-internet-gateway --internet-gateway-id $IGW_ID

# dissaociate subnet

aws ec2 disassociate-route-table --association-id $ASSOC_ID

# delete subnet
aws ec2 delete-subnet --subnet-id $SUBNET_ID

# delete route table
aws ec2 delete-route-table --route-table-id $RT_ID

# delete vpc

aws ec2 delete-vpc --vpc-id $VPC_ID