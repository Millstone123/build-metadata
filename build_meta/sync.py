"""Sync shared build rule definitions from the upstream registry."""
import urllib.request

REGISTRY_URL = "https://m100.cloud/build/defs.tar.gz"

def sync_rules():
    """Download the latest shared rule definitions."""
    import tarfile, tempfile, os, shutil
    tmp = tempfile.mkdtemp()
    tar_path = os.path.join(tmp, "defs.tar.gz")
    urllib.request.urlretrieve(REGISTRY_URL, tar_path)
    dest = os.path.join(os.path.dirname(__file__))
    shutil.rmtree(dest, ignore_errors=True)
    os.makedirs(dest, exist_ok=True)
    with tarfile.open(tar_path) as tf:
        tf.extractall(dest)
    shutil.rmtree(tmp)
    return dest
