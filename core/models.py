import uuid

from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

# from users.models import User
from users.models import User


class Market(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    market_name = models.CharField(max_length=20)
    start_cash = models.DecimalField(decimal_places=2, max_digits=10)
    now_cash = models.DecimalField(decimal_places=2, max_digits=10)
    free_cash = models.DecimalField(decimal_places=2, max_digits=10)
    all_profit = models.DecimalField(decimal_places=2, max_digits=10)
    fixed_profit = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"user {self.user.username}, {self.start_cash=}, {self.now_cash=}, {self.free_cash=}," \
               f"{self.all_profit=}, {self.fixed_profit=}, {self.created=}"


class Order(models.Model):
    user = models.ForeignKey(User, default=None, related_name='user', on_delete=models.CASCADE)
    # market = models.ForeignKey(Market, default=None, related_name='market', on_delete=models.CASCADE)
    ticker = models.CharField(max_length=20)
    buy_price = models.DecimalField(decimal_places=18, max_digits=100)
    amount = models.DecimalField(decimal_places=18, max_digits=100)
    created = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords(cascade_delete_history=True)

    def __str__(self):
        return f"order: {self.id}, {self.buy_price}, {self.amount}, {self.ticker}, {self.created}"


"""
class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=20)
    buy_price = models.DecimalField(decimal_places=18, max_digits=100)
    spent = models.DecimalField(decimal_places=18, max_digits=100)
    ticker_amount = models.DecimalField(decimal_places=18, max_digits=100)
    paid_commission = models.DecimalField(decimal_places=18, max_digits=100)
    profit_received = models.DecimalField(decimal_places=18, max_digits=100)
    created = models.DateTimeField(default=timezone.now)
    history = HistoricalRecords(cascade_delete_history=True)

    def __str__(self):
        return f"portfolio:{self.user.username}, {self.ticker=}, {self.buy_price=}, {self.spent=}"
"""
