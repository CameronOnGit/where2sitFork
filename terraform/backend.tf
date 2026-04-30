terraform {
  backend "s3" {
    bucket = "terraform-state-where2sit-rammasunw"
    key    = "core/terraform.tfstate"
    region = "us-east-2"
  }
}