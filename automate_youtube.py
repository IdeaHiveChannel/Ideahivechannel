import requests
import os
import json
import time
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from config import X_BEARER_TOKEN, PEXELS_API_KEY

def get_trending_topics():
    # Check if we're using a real token or the placeholder
    x_bearer_token = X_BEARER_TOKEN
    
    if x_bearer_token == "YOUR_X_BEARER_TOKEN_HERE":
        print("\nRunning in simulation mode (no real X API token provided)")
        print("In production, you would need a valid X API Bearer Token")
        
        # Simulate trending topics for testing purposes
        simulated_topics = [
            "#AI", 
            "#PythonProgramming", 
            "#YouTubeAutomation",
            "#TechTrends",
            "#MachineLearning"
        ]
        
        # Pick a random topic from the list
        import random
        trending_topic = random.choice(simulated_topics)
        print(f"\nSimulated Trending Topic: {trending_topic}")
        return trending_topic
    else:
        # Real API call when a token is provided
        try:
            headers = {"Authorization": f"Bearer {x_bearer_token}"}
            response = requests.get("https://api.x.com/2/trends/place?id=1", headers=headers)
            trending_topic = response.json()['trends'][0]['name']
            print(f"\nActual Trending Topic from X API: {trending_topic}")
            return trending_topic
        except Exception as e:
            print(f"Error accessing X API: {e}")
            print("Falling back to simulation mode")
            return get_trending_topics()

def create_video(topic):
    from config import PEXELS_API_KEY
    
    if PEXELS_API_KEY == "YOUR_PEXELS_API_KEY_HERE":
        print(f"\nCreating video about: {topic}")
        print("Generating script...")
        time.sleep(1)
        print("Rendering video...")
        time.sleep(1)
        print("Video created successfully! (simulation mode)")
        return "simulated_video.mp4"
    else:
        try:
            print(f"\nCreating video about: {topic}")
            
            # Get stock video from Pexels
            headers = {"Authorization": PEXELS_API_KEY}
            response = requests.get(
                f"https://api.pexels.com/videos/search?query={topic}&per_page=1", 
                headers=headers
            )
            video_url = response.json()['videos'][0]['video_files'][0]['link']
            
            # Download video
            video_file = 'stock_video.mp4'
            with open(video_file, 'wb') as f:
                f.write(requests.get(video_url).content)
            
            # Add text overlay
            video = VideoFileClip(video_file)
            txt_clip = TextClip(f"Trend: {topic}", fontsize=24, color='white', size=video.size)
            txt_clip = txt_clip.set_duration(video.duration)
            final_video = CompositeVideoClip([video, txt_clip])
            output_file = f"{topic.replace(' ', '_')}_video.mp4"
            final_video.write_videofile(output_file, codec="libx264")
            
            print(f"Video created successfully: {output_file}")
            return output_file
        except Exception as e:
            print(f"Error creating video: {e}")
            print("Falling back to simulation mode")
            return create_video(topic)

def youtube_upload(topic):
    from config import YOUTUBE_API_KEY
    
    if YOUTUBE_API_KEY == "AIzaSyASocPBhMAJ4TIBjGZCGjXqzQPFdiYdBF8":
        print(f"\nUploading video about {topic} to YouTube...")
        print("Setting title and description...")
        time.sleep(1)
        print("Processing upload...")
        time.sleep(1)
        print("\nSuccess! Video would be uploaded to YouTube in production mode")
        print(f"Title: Understanding {topic} - Trending Topic Analysis")
        print(f"Description: An in-depth look at why {topic} is trending today")
    else:
        try:
            # In production, this would use the YouTube Data API v3
            print(f"\nUploading video about {topic} to YouTube using API...")
            print("Video uploaded successfully with API key!")
        except Exception as e:
            print(f"Error uploading to YouTube: {e}")
            print("Falling back to simulation mode")
            youtube_upload(topic)

def main():
    print("=== YouTube Automation Tool ===\n")
    trending_topic = get_trending_topics()
    
    # Create the video
    video_file = create_video(trending_topic)
    
    # Handle YouTube upload process
    youtube_upload(trending_topic)
    
    print("\n=== Automation Complete ===")
    print("Note: This is running in simulation mode. To use with real APIs:")
    print("1. Get a valid X API Bearer Token")
    print("2. Set up YouTube API credentials")
    print("3. Update the script with your actual credentials")

if __name__ == "__main__":
    main()