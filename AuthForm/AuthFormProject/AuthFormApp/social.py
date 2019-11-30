from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import google.oauth2.credentials
import google_auth_oauthlib.flow
from django.http import HttpResponseRedirect
from django.views.generic import View

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


class GoogleWorker(View):
    creds = None

    def get(self,request):
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'tokens/credentials.json',SCOPES)
        flow.redirect_uri = 'https://127.0.0.1:8000/oauthcallback'
        authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')
        return HttpResponseRedirect(authorization_url)

class OAuthCallback(View):

    def get(self,request):
        self.state = request.GET.get('state')
        self.code = request.GET.get('code')
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'tokens/credentials.json', scopes=SCOPES, state=self.state)
        flow.fetch_token(authorization_response=self.code)
        credentials = flow.credentials
        service = build('gmail', 'v1', credentials=credentials)
        # Call GMAIL API method to get users email
        results = service.users().getProfile(userId='me').execute()
        email = results.get('emailAddress',[])
        return HttpResponseRedirect(f'/test/?email={email}')
