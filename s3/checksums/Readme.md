## Create a new s3 bucket

```md
aws s3 mb s3://checksums-example-ab-1232

```

```md
echo  "Hello world" > myfile.txt
```

##Get a checksum of a file for md5

md5sum myfile.txt

# f0ef7081e1539ac00ef5b761b4fb01b3  myfile.txt

## Upload file and look at its etag

```
aws s3 cp myfile.txt s3://checksums-example-ab-1232
aws s3api head-object --bucket checksums-example-ab-1232 --key myfile.txt
```
