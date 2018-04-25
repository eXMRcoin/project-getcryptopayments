import json
import requests
import datetime

from django import template
from apps.coins.utils import *

register = template.Library()


@register.simple_tag
def get_balance_BTC(user):
    balance = get_balance(user, "BTC")
    if not balance:
        balance = 0
    return balance

@register.filter
def rcv(mapping, key):
    return mapping.get('transactions_rcv_'+key, '')


@register.filter
def snd(mapping, key):
    return mapping.get('transactions_snd_'+key, '')


@register.simple_tag
def get_bal_coin(key, user):
    try:
        balance = get_balance(user, key)
    except:
        return 0
    if not balance:
        balance = 0
    return balance


@register.filter(name='unix_to_datetime')
def unix_to_datetime(value):
    try:
        date = datetime.datetime.fromtimestamp(int(value))
    except:
        date = value
    return date



