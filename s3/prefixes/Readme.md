```sh
aws s3 mb s3://prefixes-fun-adb-241412
```

```sh
aws s3api put-object \
 --bucket="prefixes-fun-adb-241412" \
 --key="myfile.txt"
```

## Create many folders

```sh
aws s3api put-object \
--bucket="prefixes-fun-adb-241412" \
--key="demo/test/myfolder/new/myfile.txt" \
--body="myfile.txt"
```