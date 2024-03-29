import boto3
from django.conf import settings
from django.core.files.storage import default_storage

def save_tool_image_to_s3(uploaded_file):
    """Saves an uploaded image of a tool's logo to an S3 bucket."""
    s3_client = boto3.client('s3')
    filename = uploaded_file.name  
    s3_client.upload_fileobj(
        uploaded_file,
        settings.AWS_STORAGE_BUCKET_NAME,
        filename,
        ExtraArgs={'ACL': 'public-read'}  
    )
    
    # Construct the S3 URL directly
    s3_url = f"{settings.AWS_STORAGE_BUCKET_NAME}.s3.{settings.AWS_S3_REGION_NAME}.amazonaws.com/{filename}"

    return s3_url