import boto3
import botocore.vendored.requests.packages.urllib3 as urllib3


    url='http://yourdownloadurl/file.tgz' # put your url here
    bucket = 'aws-s3-bucket' #your s3 bucket
    key = 'folder/filename' #your desired s3 path or filename

    s3=boto3.client('s3')
    http=urllib3.PoolManager()
    s3.upload_fileobj(http.request('GET', url,preload_content=False), bucket, key)