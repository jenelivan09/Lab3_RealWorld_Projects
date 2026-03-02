def monitor(func):
    """Decorator to log data processing status."""
    def wrapper(*args, **kwargs):
        print("Processing Started")
        result = func(*args, **kwargs)
        print("Processing Completed")
        return result
    return wrapper

def signal_shutdown(power, calls=0):
    """Recursive function to simulate signal power down."""
    if power <= 0: # Base case
        return calls
    
    print(f"Current signal strength: {power}")
    # Decrement by 1 and track recursion depth
    return signal_shutdown(power - 1, calls + 1)

def play_count_stream(limit):
    """Generator that yields squared even numbers up to the limit."""
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i ** 2