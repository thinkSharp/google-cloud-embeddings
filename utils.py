from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

def get_credentials(project_key_path):
    credentials = Credentials.from_service_account_file(project_key_path, 
                                                        scopes=['https://www.googleapis.com/auth/cloud-platform'])
    
    if credentials.expired:
        credentials.refresh(Request())

    return credentials