# Define the Cloud Provider
provider "aws" {
  region = "us-east-1" # You can change this to your preferred region
}

# Create the S3 Bucket
resource "aws_s3_bucket" "sentinel_logs" {
  bucket = "sentinel-monitor-logs-${random_id.suffix.hex}" # Must be globally unique
}

# Generate a random suffix to avoid name conflicts
resource "random_id" "suffix" {
  byte_length = 4
}

# Output the bucket name so we can use it later
output "bucket_name" {
  value = aws_s3_bucket.sentinel_logs.bucket
}
