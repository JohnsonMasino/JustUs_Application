from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login


def payment_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Replace 'YOUR_PUBLIC_KEY' with your actual FlutterWave public key
        public_key = 'FLWPUBK_TEST-3d24a64c35ed08e3149c9babab27b6ed-X'

        # Replace 'YOUR_TRANSACTION_ID' with a unique transaction ID
        transaction_id = 'YOUR_TRANSACTION_ID'

        # Replace '50' with the amount you want to charge (in the smallest currency unit)
        amount = 1000

        # Prepare the payload for the FlutterWave API
        payload = {
            'public_key': 'public_key',
            'tx_ref': transaction_id,
            'amount': 100000,
            'currency': 'NGN',
            'payment_type': 'card',
            'customer_email': email,
            'redirect_url': '',  # URL to redirect to after payment (optional)
            'meta': {
                'consumer_id': 'user_123',  # Optional metadata
            }
        }

        # Make the request to FlutterWave API (you may need to adjust the actual API endpoint)
        response = requests.post('https://api.flutterwave.com/v3/charges?type=card', json=payload)

        # Handle the response and perform any necessary actions based on success or failure
        if response.status_code == 200:
            # Payment successful, do something
            print(response.json())
            return render(request, 'success.html')  # Render a success page or redirect to a success URL
        else:
            # Payment failed, do something
            print(response.json())
            return render(request, 'error.html')  # Render an error page or redirect to an error URL

    else:
        return render(request, 'payment.html')

def google_auth(request):
    # Redirect the user to the Google OAuth consent screen
    auth_uri = f"{GOOGLE_AUTH_URI}?client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&response_type=code&scope=email%20profile"
    return redirect(auth_uri)

def google_auth_callback(request):
    # Get the authorization code from the callback
    code = request.GET.get('code')

    # Exchange the code for access and ID tokens
    token_response = requests.post(GOOGLE_TOKEN_URI, data={
        'code': code,
        'client_id': GOOGLE_CLIENT_ID,
        'client_secret': GOOGLE_CLIENT_SECRET,
        'redirect_uri': GOOGLE_REDIRECT_URI,
        'grant_type': 'authorization_code',
    })

    token_data = token_response.json()
    access_token = token_data['access_token']

    # Get user information from Google API
    user_info_response = requests.get(GOOGLE_USER_INFO, headers={'Authorization': f'Bearer {access_token}'})
    user_info = user_info_response.json()

    # Authenticate and log in the user
    user = authenticate(request, google_user_info=user_info)
    if user is not None:
        login(request, user)
        return redirect('https://github.com/JohnsonMasino')  # Replace 'home' with the URL name for your homepage

    return redirect('https://accounts.google.com/o/oauth2/auth')  # Redirect to the login page if authentication fails
def my_view(request):
    return render(request, 'auth.html')
