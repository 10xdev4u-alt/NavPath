# Infrastructure as Code for Cloud Backend
resource "aws_s3_bucket" "map_storage" {
  bucket = "navpath-maps"
}
