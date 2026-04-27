import urllib.request
import time
import os

# Define the file containing our target websites
SITES_FILE = "sites.txt"

def check_sites():
    # Phase 1 Logic: Read URLs from the text file
    if not os.path.exists(SITES_FILE):
        print(f"[ERROR] {SITES_FILE} not found!")
        return

    with open(SITES_FILE, "r") as f:
        sites = f.read().splitlines()

    print(f"--- Sentinel Monitor Started at {time.ctime()} ---")

    for site in sites:
        try:
            # Measure Latency (The time it takes to get a response)
            start_time = time.time()
            
            # Perform the HTTP check
            response = urllib.request.urlopen(site, timeout=10)
            
            # Calculate latency in milliseconds
            latency = (time.time() - start_time) * 1000
            
            # Output success to terminal (Standard SRE Status Code check)
            print(f"[SUCCESS] {site} | Status: {response.status} | Latency: {latency:.2f}ms")
            
        except Exception as e:
            # Fault Tolerance: Catch errors (DNS, SSL, or 404s) without crashing the script
            print(f"[ERROR] {site} | Failed: {e}")

if __name__ == "__main__":
    check_sites()
