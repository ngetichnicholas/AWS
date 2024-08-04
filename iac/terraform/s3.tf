resource "aws_s3_bucket" "my-s3-bucket" {
  bucket = "nickdemo002"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}