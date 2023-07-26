import requests
from django.shortcuts import render

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
            'amount': 1000,
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