# Create a bucket

aws s3 mb s3://class-fun-ab-23231


## Create a file

aws s3 cp myfile.txt s3://class-fun-ab-23231

## Change storage class

aws s3 cp myfile.txt s3://class-fun-ab-23231 --storage-class STANDARD_IA


## Clean up

aws s3 rm s3://class-fun-ab-23231/myfile.txt
aws s3 rb s3://class-fun-ab-23231