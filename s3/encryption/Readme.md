# Create a bucket

aws s3 mb s3://encrypt-fun-ab-23231


## Create a file and put the object with default SSE-S3
echo "Hello World"> myfile.txt
aws s3 cp myfile.txt s3://encrypt-fun-ab-23231

## Put an object with encryption SSE-KMS

aws s3api put-object \
--bucket encrypt-fun-ab-23231 \
--key hello.txt \
--body myfile.txt \
--server-side-encryption aws:kms \
--ssekms-key-id 9f0f3d8d-e4f3-4e52-b857-08f86e923b83

## Put object with SS3-C
openssl rand -out ssec.key 32

aws s3 cp hello.txt s3://encrypt-fun-ab-23231/hello.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key 

aws s3 cp s3://encrypt-fun-ab-23231/hello.txt hello.txt \
--sse-c AES256 \
--sse-c-key fileb://ssec.key 