def audit_log(func):
    """Decorator to log authorization status."""
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper

def compute_access_level(control, artist_len):
    """Computes access level based on the provided formula."""
    return (control * 3) + artist_len

@audit_log
def validate_access(level, threshold):
    """Compares level against threshold and returns decision."""
    if level >= threshold:
        return "ACCESS GRANTED"
    return "ACCESS DENIED"