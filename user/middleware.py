import datetime
import logging


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR','Nomalum ip')
       
        response = self.get_response(request)
        return response

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

logger = logging.getLogger('telegram')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip = get_client_ip(request)  # Bu funksiyani o'zingiz yozing yoki toping
    logger.info(f"User saytga kirdi: {user.username} (ID: {user.id}), IP: {ip}")
