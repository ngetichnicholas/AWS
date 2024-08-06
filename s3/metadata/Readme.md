## Create a bucket

```sh
aws s3 mb s3://metadata-nick-2325 
```

### Create a new file
```sh
echo "Hello world" > metadat.txt
```

### Upload the file with metadata

```sh
aws s3api put-object \
--bucket="metadata-nick-2325" \
--key="metadata.txt" \
--body="metadat.txt" \
--metadata="Planet=Earth"
```