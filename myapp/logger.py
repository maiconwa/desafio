import logging
logger = logging.getLogger(__name__)


def log_view(request):
    logger.info('User IP: %s Request Method: %s Request URL: %s' % (request.META.get('REMOTE_ADDR'), request.method, request.path))
    # Codes