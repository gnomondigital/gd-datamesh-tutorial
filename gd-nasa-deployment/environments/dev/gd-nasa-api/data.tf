data "terraform_remote_state" "foundation" {
  backend = "gcs"
  config = {
    bucket = "gd-gcp-datamesh-qa"
    prefix = "data-platform/api-gateway/foundation"
  }
}