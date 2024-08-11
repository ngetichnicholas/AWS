# Create website 1

## Create a bucket
```sh
aws s3 mb s3://cors-fun-321415
```

## Change public access

```sh
aws s3api put-public-access-block \
--bucket cors-fun-321415 \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"
```

## Create a bucket policy


```sh
aws s3api put-bucket-policy \
--bucket cors-fun-321415 \
--policy file://policy.json
```


## Turn on a static website hosting
```sh
aws s3api put-bucket-website --bucket cors-fun-321415 --website-configuration file://website.json
```

## Upload index.html file and include a resource that would be cross-origin

```sh
aws s3 cp index.html s3://cors-fun-321415
```

## View the website and see the index.html page

http://cors-fun-321415.s3-website-us-west-2.amazonaws.com/


## Create API Gateway with mock response and test the endpoint

curl -X POST https://jqk9r4v86e.execute-api.us-west-2.amazonaws.com/prod/hello \
-H "Content-Type: application/json" 

## Set cors on the bucket

```sh
aws s3api put-bucket-cors --bucket cors-fun-321415 --cors-configuration file://cors.json
```