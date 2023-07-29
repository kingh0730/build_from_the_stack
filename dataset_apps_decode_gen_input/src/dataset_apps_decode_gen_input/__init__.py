import logging


from .dataset import APPSDecodeGenInput


def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    logging.basicConfig(
        level=logging.INFO,
    )

    logger = logging.getLogger(__name__)

    apps = APPSDecodeGenInput(
        logger=logger,
    )

    return apps.dataset()
