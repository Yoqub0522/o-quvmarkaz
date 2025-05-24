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
from user_agents import parse
import logging

logger = logging.getLogger('telegram')

def get_client_info(request):
    # IP manzilini aniqlash
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', 'unknown')

    # User-Agent orqali qurilma, OS va brauzerni aniqlash
    ua_string = request.META.get('HTTP_USER_AGENT', 'unknown')
    user_agent = parse(ua_string)

    device = user_agent.device.family or "Unknown Device"
    os = f"{user_agent.os.family} {user_agent.os.version_string}" or "Unknown OS"
    browser = f"{user_agent.browser.family} {user_agent.browser.version_string}" or "Unknown Browser"

    return ip, device, os, browser

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip, device, os, browser = get_client_info(request)
    logger.info(
        f"User saytga kirdi: {user.username} (ID: {user.id}), IP: {ip}, "
        f"Qurilma: {device}, OS: {os}, Brauzer: {browser}"
    )

