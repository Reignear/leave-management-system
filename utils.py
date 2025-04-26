import os

def get_asset(filename):
    """Returns the absolute path to an asset (image, icon, etc.)."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    assets_dir = os.path.join(base_dir, "assets")
    return os.path.join(assets_dir, filename)
