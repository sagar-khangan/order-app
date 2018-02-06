# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Orders(models.Model):
    COD='COD'
    NET_BANKING='NB'
    CARD_PAYMENT='CP'
    WALLET = 'WA'
    PENDING = 'PE'
    APPROVED = 'AP'
    SHIPPED = 'SH'
    DELIVERED = 'DE'
    CANCELLED = 'CA'
    RETURN = 'RE'
    PAYMENT_METHOD_CHOICE = (
        (COD, 'Cash on Delivery'),
        (NET_BANKING, 'Net banking'),
        (CARD_PAYMENT, 'Card Payment'),
        (WALLET, 'Wallet'),
    )
    STATUS_CHOICE = (
        (PENDING, 'Order Pending'),
        (APPROVED, 'Order Approved'),
        (SHIPPED, 'Order Shipped'),
        (DELIVERED, 'Order Delivered'),
        (CANCELLED, 'Order Cancelled'),
        (RETURN, 'Order Return'),

    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_order = models.IntegerField('Total Order')
    payment_method=models.CharField(
        max_length=3,
        choices=PAYMENT_METHOD_CHOICE
    )
    status =  models.CharField(
        max_length=3,
        choices=STATUS_CHOICE
    )

class OrderItems(models.Model):
    title= models.CharField('Title', max_length=30)
    quantity = models.IntegerField('Quantity')
    price = models.FloatField('Price')
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)



