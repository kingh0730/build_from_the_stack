from .dataset import APPSDataset


def main():
    """Entry point for the application script"""
    print("Call your main application code here")

    apps = APPSDataset()
    ds = apps.dataset()
