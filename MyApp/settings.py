import os
# settings.py

# Add the following line at the top of the file
# ...
# Add or update the STATIC_URL and STATICFILES_DIRS settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'MyApp/static'),  # Replace 'myapp' with your app's name
]
# ...
# settings.py
INSTALLED_APPS = [
    # ...
    'MyApp.apps.MyAppClass' # Add your app here
    # ...
]