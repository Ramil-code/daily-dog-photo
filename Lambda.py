import boto3
import random
              
s3 = boto3.client('s3')   # Initialize the S3 client

bucket_name = 'ENTER_S3_BUCKET_NAME'

folder_name = 'REPLACE_WITH_PHOTOS_STORAGE_BUCKET/'

html_file_key = 'index.html'

cloudfront_domain = 'XXXXXXXXXXX.cloudfront.net'  # Replace this with your CloudFront domain

def get_photo_list():
  
    """Get the list of photos from the S3 bucket"""
  
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name)

    if 'Contents' not in response:
        raise Exception('No photos found in the bucket')

    photos = [obj['Key'] for obj in response['Contents']]
    
    if not photos:
        raise Exception('No photos found in the bucket')

    return photos

def choose_random_photo(photos):
  
    """Select a random photo from the list"""
    
  return random.choice(photos)

def generate_html_content(chosen_photo):
  
    """Generate HTML content to display the selected photo"""
  
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daily Dog Photo</title>
    <style>
        body {{
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }}
        img {{
            max-width: 90%;
            max-height: 90vh;
            border: 5px solid #ddd;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }}
    </style>
</head>
<body>
    <h1>Daily Dog Photo</h1>
    <img src="https://{cloudfront_domain}/{chosen_photo}" alt="Daily Dog Photo">
</body>
</html>"""

def lambda_handler(event, context):
    """Main Lambda function."""
    try:
        # Get the list of photos
        photos = get_photo_list()

        # Choose a random photo from the list
        chosen_photo = choose_random_photo(photos)

        # Generate the HTML content
        html_content = generate_html_content(chosen_photo)

        # Upload the HTML content to S3
        s3.put_object(Bucket=bucket_name, Key=html_file_key, Body=html_content, ContentType='text/html')

        return {
            'statusCode': 200,
            'body': 'HTML file updated successfully'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
