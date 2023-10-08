import boto3


resource = boto3.resource('s3')

iterator = resource.buckets.all()

print("Listing all buckets")

for bucket in iterator:
    print(bucket.name)

