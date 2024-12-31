# Daily Dog Photo Gallery 🐾

<p align="center">
  <img src="https://github.com/user-attachments/assets/932fa207-0c21-4e87-9da7-85cedad30fd7" alt="Gallery Image">
</p>

A fun project where I built an automated system for my photo hobby to display a new dog photo every day. Perfect for dog lovers who want to start their day with some furry inspiration!

## Features
- **Daily Dog Updates**: Displays a new dog photo from the collection every day (or at any specified interval) 
- **Automated Uploads**: Uses AWS Lambda to manage the photo rotation.
- **Static Website**: Hosted on AWS S3 with a simple HTML interface.
- **Mobile-Friendly**: The design adapts to any screen size.

## How It Works
1. **Photo Collection**: A set of pre-uploaded dog photos stored in an AWS S3 bucket.
2. **Photo Rotation**: An AWS Lambda function automatically shifts the photos daily.
3. **Static Website**: A static HTML page fetches the latest dog photo from S3 and displays it.
4. **Automation**: The system ensures a fresh photo appears every 24 hours.

## Technologies Used
- **AWS S3**: For storing photos and hosting the website.
- **AWS Lambda**: For automating photo rotation.
- **AWS CloudFront**: For content delivery and ensuring faster access to the website and photos globally.
- **HTML/CSS**: For the static web page.

## Screenshot
<p align="center">
  <img src="https://github.com/user-attachments/assets/80787775-d218-440d-84de-b188115ddd26" alt="Gallery Screenshot">
</p>

## How to Run the Project

### Step 1: Deploy the S3 Website
1. **Create an S3 Bucket**:
   - Go to the AWS S3 console and create a new bucket.
   - Make sure the bucket name is globally unique.
2. **Enable Static Website Hosting**:
   - Go to the "Properties" tab of your S3 bucket.
   - Under "Static website hosting", select **Enable**.
   - Set `index.html` as the default page.
3. **Upload Photos and HTML**:
   - Create a folder in the bucket (for example, `my-daily-photo-bucket`).
   - Upload your photos to this folder.
4. **IAM Permissions**:
   - Ensure the S3 bucket has the correct IAM permissions and CORS settings to allow public access to the HTML and photo files.

### Step 2: Set Up CloudFront Distribution
1. **Create a CloudFront Distribution**:
   - Go to the AWS CloudFront console.
   - Create a new distribution and select your S3 bucket as the origin.
   - Set the distribution settings according to your needs (Caching/TTL)
2. **Update the CloudFront Domain**:
   - After the CloudFront distribution is created, you'll get a CloudFront domain (e.g., `xxxxxxxx.cloudfront.net`).

### Step 3: Set Up the Lambda Function
1. **Use Lambda Script**:
   - Use the `lambda.py` script to create an AWS Lambda function.
   - IAM Permissions: Ensure that your Lambda function has the necessary permissions to access S3. The policy should allow s3:ListBucket and s3:PutObject actions on the target bucket.
   - Set the function to run daily using AWS CloudWatch Events trigger (Amazon EventBridge)

### Step 3: Upload Your Dog Photos
1. **Upload 12 Dog Photos**:
   - Upload photos to your S3 bucket

### Step 5: Enjoy the Gallery
1. **Access via CloudFront**:
   - After everything is set up, visit your website using the CloudFront URL to see the new dog photo every day!
