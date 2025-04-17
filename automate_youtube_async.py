import asyncio
import aiohttp
import os
import time
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from config import X_BEARER_TOKEN, PEXELS_API_KEY, YOUTUBE_API_KEY
from youtube_api import get_authenticated_service, upload_video

# Retry decorator for robustness
@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type((aiohttp.ClientError, HttpError)))
async def fetch_trending_topics(session):
    if X_BEARER_TOKEN == "YOUR_X_BEARER_TOKEN_HERE":
        print("\nRunning in simulation mode (no real X API token provided)")
        import random
        return random.choice(["#AI", "#PythonProgramming", "#YouTubeAutomation", "#TechTrends", "#MachineLearning"])
    else:
        async with session.get("https://api.x.com/2/trends/place?id=1", headers={"Authorization": f"Bearer {X_BEARER_TOKEN}"}) as response:
            data = await response.json()
            return data['trends'][0]['name']

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10), retry=retry_if_exception_type(aiohttp.ClientError))
async def fetch_pexels_video(session, topic):
    if PEXELS_API_KEY == "YOUR_PEXELS_API_KEY_HERE":
        print(f"\nCreating video about: {topic} (simulation mode)")
        time.sleep(1)
        return "simulated_video.mp4"
    else:
        async with session.get(f"https://api.pexels.com/videos/search?query={topic}&per_page=1", headers={"Authorization": PEXELS_API_KEY}) as response:
            data = await response.json()
            video_url = data['videos'][0]['video_files'][0]['link']
            async with session.get(video_url) as video_response:
                with open('stock_video.mp4', 'wb') as f:
                    f.write(await video_response.read())
            video = VideoFileClip('stock_video.mp4')
            txt_clip = TextClip(f"Trend: {topic}", fontsize=24, color='white', size=video.size).set_duration(video.duration)
            output_file = f"{topic.replace(' ', '_')}_video.mp4"
            final_video = CompositeVideoClip([video, txt_clip])
            final_video.write_videofile(output_file, codec="libx264")
            return output_file

async def main():
    print("=== YouTube Automation Tool ===\n")
    async with aiohttp.ClientSession() as session:
        trending_topic = await fetch_trending_topics(session)
        print(f"Trending Topic: {trending_topic}")
        video_file = await fetch_pexels_video(session, trending_topic)
        youtube = get_authenticated_service()
        upload_video(youtube, video_file, f"Understanding {trending_topic}", f"An in-depth look at why {trending_topic} is trending today", 'public')
    print("\n=== Automation Complete ===")

if __name__ == "__main__":
    asyncio.run(main())