data "terraform_remote_state" "foundation" {
  backend = "gcs"
  config = {
    bucket = "gd-gcp-datamesh-dev"
    prefix = "data-platform/api-gateway/omniweb-api"   
  }
}