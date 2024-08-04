#!/usr/bin/env bash

echo "== Delete Stack for s3 bucket =="

STACK_NAME="nicks3demo"

aws cloudformation delete-stack \
    --stack-name $STACK_NAME \
    --region us-east-1 \
