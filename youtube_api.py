from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
import os
import pickle

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
TOKEN_PICKLE_FILE = 'token.pickle'
CLIENT_SECRETS_FILE = 'client_secrets.json'

def get_authenticated_service():
    credentials = None
    
    # Load saved credentials if they exist
    if os.path.exists(TOKEN_PICKLE_FILE):
        with open(TOKEN_PICKLE_FILE, 'rb') as token:
            credentials = pickle.load(token)
    
    # If no valid credentials, let user login
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            if not os.path.exists(CLIENT_SECRETS_FILE):
                raise FileNotFoundError(
                    f'Missing {CLIENT_SECRETS_FILE}. Please download it from Google Cloud Console.'
                )
            
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRETS_FILE, SCOPES)
            credentials = flow.run_local_server(port=0)
            
        # Save credentials for future use
        with open(TOKEN_PICKLE_FILE, 'wb') as token:
            pickle.dump(credentials, token)
    
    return build('youtube', 'v3', credentials=credentials)

def upload_video(youtube, file_path, title, description, privacy_status='private'):
    try:
        # Validate file exists and is accessible
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Video file not found: {file_path}")
            
        # Prepare video metadata
        body = {
            'snippet': {
                'title': title,
                'description': description,
                'tags': ['automation', 'trending', 'analysis']
            },
            'status': {
                'privacyStatus': privacy_status,
                'selfDeclaredMadeForKids': False,
            }
        }
    except Exception as e:
        print(f"Error preparing video metadata: {e}")
        return None
    
    insert_request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=MediaFileUpload(
            file_path, 
            chunksize=-1, 
            resumable=True
        )
    )
    
    response = None
    while response is None:
        try:
            _, response = insert_request.next_chunk()
            if response:
                print(f'Video uploaded successfully! Video ID: {response["id"]}')
                return response
        except Exception as e:
            print(f'An error occurred: {e}')
            return None