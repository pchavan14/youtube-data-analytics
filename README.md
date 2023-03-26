Prerequisities - Python , AWS s3, AWS glue crawler ( the crawler scans the data in S3, infers the schema and creates a table in glue catalog) , AWS Athena, AWS Lambda




An error occureded while uploading files into S3 bucket - An error occurred (AccessDenied) when calling the CreateMultipartUpload operation: Access Denied

Resolutions

Workaround is to avoid multi-part uploads, by either:

    Increase your triggering limit for s3 cp command from the default 8MB to higher, e.g. 5GB (see https://docs.aws.amazon.com/cli/latest/topic/s3-config.html)
    Use aws s3api put-object instead - it doesn't automatically switch to multi-part uploads.

Multi-part uploads are auto-enabled in s3 cp for performance and fault-tolerancy.

AWS glue needs JSON in one line , so to do that we will convert the JSON file into apache parquet format using aws lambda


IAM permission errors needs to be resolved

When selecting crawler , select the subfolder with the files

Parquet file comes with metadata , when we change the datatype inside aws catalog it does not change the datatype


