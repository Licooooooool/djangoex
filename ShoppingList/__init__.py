# coding:utf-8\

from django.apps import AppConfig
import os

default_app_config = 'ShoppingCar.ShoppingcarConfig'

VERBOSE_APP_NAME = "订单"


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class ShoppingcarConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME