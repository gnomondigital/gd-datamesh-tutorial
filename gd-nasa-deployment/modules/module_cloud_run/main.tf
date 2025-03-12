#-------------------------------------------------------------------------------
# TO DEPLOY CLOUD RUN
#-------------------------------------------------------------------------------

locals {
  google_service_account = var.api_run_sa
}

resource "google_cloud_run_v2_service" "this" {

  name     = var.api_name
  location = var.region

  template {
    containers {
      image = var.image_name
      args  = var.image_args

      resources {
        limits = {
          # Memory usage limit (per container)
          memory = var.memory_limit
          # CPI usage limit (per container)
          cpu = var.cpu_limit
        }
      }

      liveness_probe {
        http_get {
          path = "/"
        }
      }
    }
    service_account = local.google_service_account
  }
}
#-------------------------------------------------------------------------------
#                              --- END ---
#-------------------------------------------------------------------------------
