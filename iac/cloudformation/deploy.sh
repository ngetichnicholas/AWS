#!/usr/bin/env bash

echo "== Deploy an S3 Bucket =="

STACK_NAME="nicks3demo"

aws cloudformation deploy \
    --template-file template.yaml \
    --no-execute-changeset \
    --region us-east-1 \
    --stack-name $STACK_NAME