#-------------------------------------------------------------------------------
# PROVIDER
#-------------------------------------------------------------------------------
provider "google" {
  project = var.project_id
  region  = var.region
}

provider "google-beta" {
  project = var.project_id
  region  = var.region
}

terraform {
  required_version = ">=1.5.3"
  backend "gcs" {
    bucket = "gd-gcp-datamesh-qa"
    prefix = "data-platform/api-gateway/omniweb-api"
  }

}
#-------------------------------------------------------------------------------
#                              --- END ---
#-------------------------------------------------------------------------------
