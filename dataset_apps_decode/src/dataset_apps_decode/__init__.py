import logging


from .dataset import APPSDecode


def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    logging.basicConfig(
        level=logging.INFO,
    )

    logger = logging.getLogger(__name__)

    apps = APPSDecode(
        logger=logger,
    )

    global ds
    ds = apps.dataset()
