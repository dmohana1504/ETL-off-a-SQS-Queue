import hashlib

def mask_data(value: str) -> str:
    """Mask sensitive data using SHA-256 hash."""
    return hashlib.sha256(value.encode()).hexdigest()
