# Daily Dog Photo Gallery 🐾

![2121](https://github.com/user-attachments/assets/74806647-b0c5-4167-b7f9-6b81ba700261)

A fun project where I built an automated system for my photo hobby to display a new dog photo every day. Perfect for dog lovers who want to start their day with some furry inspiration!

## Features
- **Daily Dog Updates**: Displays a new dog photo from the collection every day.
- **Automated Uploads**: Uses AWS Lambda to manage the photo rotation.
- **Static Website**: Hosted on AWS S3 with a simple HTML interface.
- **Mobile-Friendly**: The design adapts to any screen size.

## How It Works
1. **Photo Collection**: A set of pre-uploaded dog photos stored in an AWS S3 bucket.
2. **Photo Rotation**: An AWS Lambda function automatically shifts the photos daily, renaming them to follow a specific order.
3. **Static Website**: A static HTML page fetches the latest dog photo from S3 and displays it.
4. **Automation**: The system ensures a fresh photo appears every 24 hours.

## Screenshot
![Daily Dog Photo Gallery Screenshot](screenshot.png)

## Technologies Used
- **AWS S3**: For storing photos and hosting the website.
- **AWS Lambda**: For automating photo rotation.
- **HTML/CSS**: For the static web page.


## How to Run the Project

### Step 1: Clone the Repository
First, clone the project repository to your local machine:
```bash
git clone https://github.com/yourusername/daily-dog-gallery.git
cd daily-dog-gallery
