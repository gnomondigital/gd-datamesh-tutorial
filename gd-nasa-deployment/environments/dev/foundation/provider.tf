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
  backend "gcs" {
    bucket = "gd-gcp-datamesh-dev"
    prefix = "data-platform/api-gateway/omniweb-api"
  }
}
#-------------------------------------------------------------------------------
#                              --- END ---
#-------------------------------------------------------------------------------
