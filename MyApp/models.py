from django.db import models

class Transaction(models.Model):
    # Fields for the Transaction model
    email = models.EmailField()  # The email associated with the transaction
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # The transaction amount
    currency = models.CharField(max_length=3)  # Currency code (e.g., USD, EUR)
    payment_type = models.CharField(max_length=20)  # Type of payment (e.g., card, bank transfer)
    transaction_id = models.CharField(max_length=50, unique=True)  # Unique transaction ID
    timestamp = models.DateTimeField(auto_now_add=True)  # Timestamp of when the transaction was created

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Amount: {self.amount} {self.currency}"