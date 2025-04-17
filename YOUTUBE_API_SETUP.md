# Setting Up YouTube API for Video Upload

This guide will help you set up the YouTube Data API v3 for automated video uploads.

## Prerequisites
- A Google Account
- A Google Cloud Project
- Python 3.9 or higher

## Setup Steps

1. **Create a Google Cloud Project**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Click "Create Project" or select an existing project
   - Note down your Project ID

2. **Enable the YouTube Data API**
   - In your project, go to "APIs & Services" > "Library"
   - Search for "YouTube Data API v3"
   - Click "Enable"

3. **Configure OAuth 2.0**
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Choose "Desktop Application" as the application type
   - Enter a name for your OAuth client
   - Click "Create"

4. **Download Credentials**
   - After creating the OAuth client, download the client configuration
   - Rename the downloaded file to `client_secrets.json`
   - Place it in your project's root directory

5. **Install Required Packages**
   ```bash
   pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

6. **First-Time Authentication**
   - Run the script (`automate_youtube.py`)
   - A browser window will open asking you to log in to your Google account
   - Grant the requested permissions
   - The script will save the credentials for future use

## Important Notes
- Keep your `client_secrets.json` file secure and never commit it to version control
- The first video upload will require manual authentication
- Videos are uploaded as "private" by default for safety
- You can change the privacy status in the `youtube_upload()` function

## Troubleshooting
- If you get a "Token has been expired or revoked" error, delete the `token.pickle` file and re-authenticate
- Make sure your Google account has a YouTube channel
- Check that you've enabled the YouTube Data API in your Google Cloud Console

## Rate Limits
- The YouTube Data API has quotas and rate limits
- Monitor your usage in the Google Cloud Console
- Consider implementing retry logic for failed uploads