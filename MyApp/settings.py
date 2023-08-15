from google.oauth2 import id_token
from google.auth.transport import requests
from django.http import JsonResponse
import os
from django.urls import path, include

urlpatterns = [
    ...
    path("", include("allauth.urls")), #most important
]
GOOGLE_CLIENT_ID = '194126296216-d9mb370ftl855uerf4p77740e1q2bc90.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = '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'
GOOGLE_REDIRECT_URI = 'http://localhost:63342/JustUs_WebApp/MyApp/Templates/payment.html?_ijt=r70hnk3ch4vr71dgkl0cp9ki9&_ij_reload=RELOAD_ON_SAVE'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'MyApp/static'),
]
# settings.py

SITE_ID = 1

INSTALLED_APPS = [
    'MyApp',
    'MyApp.apps.MyAppClass',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

SOCIALACCOUNT_LOGIN_ON_GET=True

AUTHENTICATION_BACKENDS = [
    ...
    'allauth.account.auth_backends.AuthenticationBackend'
    ]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

GOOGLE_AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
GOOGLE_TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
GOOGLE_USER_INFO = 'https://www.googleapis.com/oauth2/v1/userinfo'
