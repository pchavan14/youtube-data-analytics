import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": [
            "s3://db-on-youtube-raw-us-east-1-athena/Unsaved/2023/03/25/83ba951c-c889-44fe-9042-86ea4a9b285d.csv"
        ],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",

)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("video_id", "string", "video_id", "string"),
        ("trending_date", "string", "trending_date", "string"),
        ("title", "string", "title", "string"),
        ("channel_title", "string", "channel_title", "string"),
        ("category_id", "string", "category_id", "string"),
        ("publish_time", "string", "publish_time", "string"),
        ("tags", "string", "tags", "string"),
        ("views", "string", "views", "string"),
        ("likes", "string", "likes", "string"),
        ("dislikes", "string", "dislikes", "string"),
        ("comment_count", "string", "comment_count", "string"),
        ("thumbnail_link", "string", "thumbnail_link", "string"),
        ("comments_disabled", "string", "comments_disabled", "string"),
        ("ratings_disabled", "string", "ratings_disabled", "string"),
        ("video_error_or_removed", "string", "video_error_or_removed", "string"),
        ("description", "string", "description", "string"),
        ("region", "string", "region", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node2,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://db-on-youtube-cleansed-us-east-1-dev/raw_statistics/",
        "partitionKeys": ["region"],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()
