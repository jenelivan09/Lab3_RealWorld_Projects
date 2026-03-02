SEED_NUM = 0
FAVORITE_ARTIST = "HARRY STYLES"  
CONTROL_NUM = max(1, SEED_NUM)   
from access_control import compute_access_level, validate_access
from media_engine import signal_shutdown, play_count_stream, monitor

# --- Task 1: Authorization ---
artist_len = len(FAVORITE_ARTIST)
acc_level = compute_access_level(CONTROL_NUM, artist_len)
threshold = CONTROL_NUM * 5
decision = validate_access(acc_level, threshold)

print(f"--- Task 1 Assessment Data ---")
print(f"CONTROL_NUM: {CONTROL_NUM}")
print(f"Access Level: {acc_level}")
print(f"Threshold: {threshold}")
print(f"Decision: {decision}\n")

# --- Task 2: Recursive Shutdown ---
# Initialize power
initial_power = CONTROL_NUM + artist_len
total_calls = signal_shutdown(initial_power)

print(f"\n--- Task 2 Assessment Data ---")
print(f"Initial Power: {initial_power}")
print(f"Total Recursive Calls: {total_calls}\n")

# --- Task 3: Streaming Analytics ---
@monitor
def run_analytics(limit):
    """Processes stream and aggregates data."""
    total_plays = 0
    records = 0
    # Process generator
    for count in play_count_stream(limit):
        total_plays += count
        records += 1
    return total_plays, records

stream_limit = CONTROL_NUM + artist_len
total_p, num_r = run_analytics(stream_limit)

print(f"\n--- Task 3 Assessment Data ---")
print(f"Stream Limit: {stream_limit}")
print(f"Total Plays: {total_p}")
print(f"Records Processed: {num_r}")