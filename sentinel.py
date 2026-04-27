import urllib.request
import time
import os
import boto3  # <--- NEW: Import the AWS SDK

# CONFIGURATION
SITES_FILE = "sites.txt"
LOG_FILE = "monitor.log"
# REPLACE THIS with the 'bucket_name' from your Terraform output
S3_BUCKET_NAME = "sentinel-monitor-logs-d91fb0fe" 

def check_sites():
    s3_client = boto3.client('s3') # <--- Initialize S3 connection
    
    with open(SITES_FILE, "r") as f:
        sites = f.read().splitlines()

    # Open the log file in 'append' mode to keep history
    with open(LOG_FILE, "a") as log:
        log.write(f"--- Check started at {time.ctime()} ---\n")
        
        for site in sites:
            try:
                start_time = time.time()
                response = urllib.request.urlopen(site, timeout=10)
                latency = (time.time() - start_time) * 1000
                
                result = f"[SUCCESS] {site} | Status: {response.status} | Latency: {latency:.2f}ms\n"
                print(result.strip())
                log.write(result)
                
            except Exception as e:
                error_msg = f"[ERROR] {site} | Failed: {e}\n"
                print(error_msg.strip())
                log.write(error_msg)

    # PHASE 4 ACTION: Upload the log file to the Cloud
    try:
        print(f"Uploading {LOG_FILE} to S3...")
        s3_client.upload_file(LOG_FILE, S3_BUCKET_NAME, LOG_FILE)
        print("[CLOUD] Upload complete! Data is now persistent.")
    except Exception as e:
        print(f"[CLOUD ERROR] Failed to upload to S3: {e}")

if __name__ == "__main__":
    check_sites()      
