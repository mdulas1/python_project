from django.db import models # type: ignore

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

class Listing(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    telecom_provider = models.CharField(max_length=50)  # e.g., "MTN", "Airtel"
    value = models.DecimalField(max_digits=10, decimal_places=2)  # e.g., 500MB/₦1000
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default="pending")  # pending/active/sold

class Transaction(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

# serializers.py
from rest_framework import serializers # type: ignore
from data_airtime import Listing # type: ignore

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'seller', 'telecom_provider', 'value', 'price']

# views.py
from rest_framework import generics # type: ignore
from data_airtime import Listing
from data_airtime import ListingSerializer

class ListingAPI(generics.ListCreateAPIView):
    queryset = Listing.objects.filter(status="active")
    serializer_class = ListingSerializer

# fraud_detection.py
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_fraud(transaction_data):
    # Load transaction history
    df = pd.DataFrame(transaction_data)
    model = IsolationForest(contamination=0.01)
    df['is_fraud'] = model.fit_predict(df[['amount', 'frequency']])
    return df[df['is_fraud'] == -1]

# telecom.py
import requests
import pandas as pd
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

def get_provider_url(provider):
    try:
        return settings.TELECOM_PROVIDERS[provider]
    except KeyError:
        raise ImproperlyConfigured(f"Provider URL for {provider} not found in settings.")

def transfer_airtime(provider, recipient, amount):
    API_KEY = "YOUR_PROVIDER_KEY"
    url = f"{provider}/api/transfer"
    payload = {
        "recipient": recipient,
        "amount": amount
    }
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(url, json=payload, headers=headers)
    return response.json()