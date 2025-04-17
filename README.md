# YouTube Automation Project

This project automates the process of creating and uploading YouTube videos based on trending topics from X (formerly Twitter).

## Project Structure

- `automate_youtube.py`: Main Python script that fetches trending topics and handles video creation/upload
- `requirements.txt`: List of Python dependencies needed for the project
- `.github/workflows/daily.yml`: GitHub Actions workflow file for daily automation
- `.gitignore`: Specifies files to be ignored by Git

## Setup Instructions

1. Install Python dependencies:
   ```
   py -m pip install -r requirements.txt
   ```

2. Get your X (Twitter) API credentials (optional for simulation mode):
   - Create a developer account at https://developer.twitter.com
   - Create a project and app to get your Bearer Token
   - Replace `YOUR_X_BEARER_TOKEN_HERE` in the script with your actual token

3. (Coming soon) Set up YouTube API credentials:
   - Create a project in Google Cloud Console
   - Enable the YouTube Data API
   - Create OAuth credentials
   - Download the client secrets file

## Usage

Run the main script:
```
py automate_youtube.py
```

The script currently runs in simulation mode, which doesn't require API credentials. It will:
1. Generate a simulated trending topic
2. Simulate video creation process
3. Simulate YouTube upload process

## Features

- [x] Fetch trending topics from X (Twitter)
  - [x] Simulation mode for testing without API credentials
  - [ ] Production mode using real X API
- [x] Generate video content based on trending topics (simulation)
- [x] Upload videos to YouTube automatically (simulation)
- [ ] Implement actual video creation functionality
- [ ] Implement actual YouTube upload functionality

## Future Enhancements

- Add scheduling capabilities
- Implement analytics tracking
- Add customization options for video creation

## GitHub Repository Setup

1. Create a new repository on GitHub:
   - Go to github.com and sign in or sign up (free)
   - Click the "+" icon in the top right and choose "New repository"
   - Name it YouTubeAutomation (or match your folder name)
   - Check "Public" (for free GitHub Actions)
   - Check "Add a README file", "Add .gitignore" (choose Python), and "Choose a license" (select MIT)
   - Click "Create repository"

2. Upload your local files to GitHub:
   - On the repository page, click "Add file" > "Upload files"
   - Drag your files (automate_youtube.py, requirements.txt, etc.) into the upload area
   - Click "Commit changes"

## GitHub Actions Automation

This project includes a GitHub Actions workflow file (`.github/workflows/daily.yml`) that automatically runs the script daily at 12:00 AM UTC. The workflow:

1. Sets up a Python environment
2. Installs the required dependencies
3. Runs the automation script

No additional setup is required for the automation to work once your files are uploaded to GitHub.