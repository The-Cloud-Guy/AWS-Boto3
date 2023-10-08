import boto3

#Delete bucket with aws resource

resource = boto3.resource('s3')

bucket_name = "parwizforogh7777"

s3_bucket =resource.Bucket(bucket_name)

s3_bucket.delete()

print(" This {} bucket has been deleted  ".format(s3_bucket))
